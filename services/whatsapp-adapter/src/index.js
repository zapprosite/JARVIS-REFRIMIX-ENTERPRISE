const express = require('express');
const pino = require('pino');
const pinoHttp = require('pino-http');
const Redis = require('ioredis');
const axios = require('axios');

const logger = pino({
    level: process.env.LOG_LEVEL || 'info',
    timestamp: pino.stdTimeFunctions.isoTime,
});

const app = express();
app.use(express.json());
app.use(pinoHttp({ logger }));

const PORT = process.env.PORT || 3001;
const ORCHESTRATOR_URL = process.env.ORCHESTRATOR_URL || 'http://orchestrator-langgraph:8000';
const REDIS_URL = process.env.REDIS_URL || 'redis://redis:6379';

const redis = new Redis(REDIS_URL);

// Rate Limit Middleware
const rateLimit = async (req, res, next) => {
    const tenantId = req.headers['x-tenant-id'] || 'default';
    const key = `rate_limit:${tenantId}`;

    // Simple fixed window for demo. Production should use the 'rate_limit_guard' skill logic
    // Here we just check a simple counter
    const limit = 100; // default limit

    try {
        const current = await redis.incr(key);
        if (current === 1) {
            await redis.expire(key, 86400); // 1 day
        }

        if (current > limit) {
            logger.warn({ tenantId }, 'Rate limit exceeded');
            return res.status(429).json({ error: 'Rate limit exceeded' });
        }
        next();
    } catch (err) {
        logger.error(err, 'Redis error');
        // Fail open or closed? Open for now to not block traffic if Redis dies
        next();
    }
};

app.get('/health', (req, res) => {
    res.status(200).json({ status: 'ok', service: 'whatsapp-adapter' });
});

// Receive Webhook from WhatsApp Provider (e.g., Evolution API)
app.post('/webhook/wa', rateLimit, async (req, res) => {
    const { from, body, tenantId } = req.body;
    logger.info({ from, tenantId }, 'Received message');

    // Forward to Orchestrator
    try {
        // Fire and forget or wait? Let's wait to return success
        // In prod, push to Queue (RabbitMQ/Redpanda)
        await axios.post(`${ORCHESTRATOR_URL}/v1/chat`, {
            messages: [{ role: "user", content: body }],
            tenant_id: tenantId || "default",
            user_id: from
        });

        res.status(200).json({ status: 'queued' });
    } catch (err) {
        logger.error(err, 'Failed to forward to orchestrator');
        res.status(502).json({ error: 'Orchestrator unavailable' });
    }
});

// Stub for sending message back to user (called by Orchestrator)
app.post('/send', async (req, res) => {
    const { to, content } = req.body;
    logger.info({ to }, 'Sending WhatsApp message');
    // Implement actual call to Evolution API/Twilio here
    res.json({ status: 'sent', to });
});

app.listen(PORT, () => {
    logger.info(`WhatsApp Adapter listening on port ${PORT}`);
});
