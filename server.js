import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

// Serve static assets from the root directory
app.use(express.static(path.join(__dirname, '.')));

// Route to serve your HTML page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Dedicated API status endpoint
app.get('/api/status', (req, res) => {
    res.json({
        "name": "It's a Plan api",
        "status": "ok"
    });
});

app.listen(process.env.PORT || 3002, () => {
    console.log('proj1 listening on 3002');
});
