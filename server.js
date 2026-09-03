const express = require('express');
const path = require('path');
const app = express();

// 1. (Optional) Serve extra static files like CSS or JS images if you have them
app.use(express.static(path.join(__dirname, '.')));

// 2. Change the root route to send your actual HTML page instead of raw JSON
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// 3. Keep your API status on a dedicated API route instead
app.get('/api/status', (req, res) => {
    res.json({
        "name": "It's a Plan api",
        "status": "ok"
    });
});

app.listen(process.env.PORT || 3000, () => {
    console.log('proj1 listening on port');
});
