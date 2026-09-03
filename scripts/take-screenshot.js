import puppeteer from 'puppeteer';

// Import our server from root
import('./../server.js').then(async () => {
    console.log('Server started for screenshot...');
    await new Promise(resolve => setTimeout(resolve, 1500));

    try {
        const browser = await puppeteer.launch({
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        const page = await browser.newPage();
        await page.setViewport({ width: 1280, height: 800 });
        await page.goto('http://localhost:3002', { waitUntil: 'networkidle0' });
        await page.screenshot({ path: 'screenshot.png', fullPage: true });
        await browser.close();
        console.log('SCREENSHOT_SUCCESS: screenshot.png');
    } catch (err) {
        console.error('Screenshot error:', err);
    }
    process.exit(0);
});
