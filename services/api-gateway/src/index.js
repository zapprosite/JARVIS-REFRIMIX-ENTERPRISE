const express = require('express');
const pino = require('pino');
const pinoHttp = require('pino-http');
const cors = require('cors');
const helmet = require('helmet');
const { createProxyMiddleware } = require('http-proxy-middleware');

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => {
      return { level: label.toUpperCase() };
    },
  },
  timestamp: pino.stdTimeFunctions.isoTime,
});

const app = express();

app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(pinoHttp({ logger }));

// Guardrails Middleware (WAF-lite)
const guardrails = (req, res, next) => {
  if (req.method !== 'POST' && req.method !== 'PUT') return next();

  const payload = JSON.stringify(req.body || {});

  // 1. Size Limit (redundant with express limit, but explicit)
  if (payload.length > 10000) {
    logger.warn({ event: 'security_block', reason: 'payload_too_large' }, 'Blocked large payload');
    return res.status(413).json({ error: 'Payload too large' });
  }

  // 2. SQL Injection Patterns (Basic)
  const sqlPattern = /(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION)\b.*\b(FROM|INTO|TABLE)\b)|(--\s)/i;
  if (sqlPattern.test(payload)) {
    logger.warn({ event: 'security_block', reason: 'sqli_attempt' }, 'Blocked SQL Injection attempt');
    return res.status(403).json({ error: 'Malicious content detected' });
  }

  // 3. Prompt Injection Keywords (Defense in Depth)
  const injectionPattern = /ignore previous instructions|system override|delete system behavior/i;
  if (injectionPattern.test(payload)) {
    logger.warn({ event: 'security_block', reason: 'prompt_injection' }, 'Blocked Prompt Injection');
    return res.status(403).json({ error: 'Unsafe input detected' });
  }

  next();
};

app.use(guardrails);

const PORT = process.env.PORT || 3000;

// Health Check
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', service: 'api-gateway' });
});

// Proxy to WhatsApp Adapter
// POST /v1/messages -> WhatsApp Adapter
app.post('/v1/messages', createProxyMiddleware({
  target: process.env.WHATSAPP_ADAPTER_URL || 'http://whatsapp-adapter:3001',
  changeOrigin: true,
  pathRewrite: {
    '^/v1/messages': '/webhook/wa', // Assuming adapter listens on /webhook/wa
  },
  onProxyReq: (proxyReq, req, res) => {
    if (req.body) {
      const bodyData = JSON.stringify(req.body);
      // createProxyMiddleware streams request, so we need to restream body if parsed
      proxyReq.setHeader('Content-Type', 'application/json');
      proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData));
      proxyReq.write(bodyData);
    }
  }
}));

// Fallback
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});

app.listen(PORT, () => {
  logger.info(`API Gateway listening on port ${PORT}`);
});
