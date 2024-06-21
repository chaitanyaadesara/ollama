const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

app.get('/', async (req, res) => {
    res.json("hello from ollama");
});

app.post('/ask', async (req, res) => {
    const data = req.body;
    const prompt = data.prompt;
    console.log(prompt);

    if (!prompt) {
        return res.status(400).json({ error: "No prompt provided" });
    }

    const responses = [];
    const errors = [];
    const urls = [
        "http://localhost:11431/api/generate",
        "http://localhost:11432/api/generate",
        "http://localhost:11433/api/generate",
    ];
    const models = [
        "llama3",
        "phi3",
        "mistral"
    ];

    for (let i = 0; i < urls.length; i++) {
        try {
            const url = urls[i];
            const payload = {
                model: models[i],
                prompt: prompt
            };
            const headers = {
                "Content-Type": "application/json"
            };
            const response = await axios.post(url, payload, { headers: headers });
            let resText = response.data;
            resText = resText.replace(/}/g, '},').trim();
            if (resText.endsWith(',,') || resText.endsWith('},')) {
                resText = resText.slice(0, -1);
            }
            if (response.status === 200) {
                responses.push({
                    model: models[i],
                    resp: JSON.parse('[' + resText + ']')
                });
            }
        } catch (error) {
            console.error(error);
            errors.push({
                model: models[i],
                error: error.message
            });
        }
        res.json([responses, errors]);
    }
});

app.listen(5000, () => {
    console.log('Server is running on port 5000');
});
