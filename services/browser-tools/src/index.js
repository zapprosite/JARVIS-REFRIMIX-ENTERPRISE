const express = require('express');
const puppeteer = require('puppeteer');
const pino = require('pino');
const pinoHttp = require('pino-http');
const path = require('path');

const logger = pino({ level: 'info' });
const app = express();
app.use(express.json());
app.use(pinoHttp({ logger }));

const PORT = process.env.PORT || 3000;
const USER_DATA_DIR = process.env.USER_DATA_DIR || '/app/profile';

app.get('/health', (req, res) => {
    res.json({ status: 'ok', service: 'browser-tools' });
});

app.post('/search', async (req, res) => {
    const { query } = req.body;
    if (!query) {
        return res.status(400).json({ error: 'Query required' });
    }

    let browser;
    try {
        logger.info({ query }, 'Launching browser for search');

        browser = await puppeteer.launch({
            headless: 'new',
            userDataDir: USER_DATA_DIR,
            args: [
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage', // critical for docker
            ]
        });

        const page = await browser.newPage();
        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');

        // Simple Google Search
        await page.goto(`https://www.google.com/search?q=${encodeURIComponent(query)}`, { waitUntil: 'domcontentloaded' });

        // Extract results (simple selector, might break)
        const results = await page.evaluate(() => {
            const items = document.querySelectorAll('.tF2Cxc'); // Common Google result class
            const data = [];
            items.forEach(item => {
                const title = item.querySelector('h3')?.innerText;
                const link = item.querySelector('a')?.href;
                const snippet = item.querySelector('.VwiC3b')?.innerText;
                if (title && link) {
                    data.push({ title, link, snippet });
                }
            });
            return data;
        });

        // If google fails or blocks, fallback logic would go here

        res.json({ results });

    } catch (err) {
        logger.error(err, 'Browser error');
        res.status(500).json({ error: err.message });
    } finally {
        if (browser) {
            await browser.close();
        }
    }
});

app.listen(PORT, () => {
    logger.info(`Browser Tools listening on port ${PORT}`);
});
