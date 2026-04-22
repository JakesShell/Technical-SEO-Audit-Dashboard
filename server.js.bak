// server/server.js
const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());
app.use(express.static('../public'));

app.post('/api/audit', async (req, res) => {
    const { url } = req.body;

    try {
        // Replace with actual API calls to Google PageSpeed Insights and Moz
        const pageSpeedResponse = await axios.get(`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${url}&key=YOUR_API_KEY`);
        
        // Mock response for demonstration
        const auditResults = {
            speed: pageSpeedResponse.data.lighthouseResult.categories.performance.score * 100,
            mobileFriendly: pageSpeedResponse.data.lighthouseResult.categories.seo.score * 100,
            // Add more metrics as needed
        };

        res.json(auditResults);
    } catch (error) {
        res.status(500).json({ error: 'An error occurred while fetching data.' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
