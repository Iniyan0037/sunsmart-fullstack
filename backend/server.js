const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = 3000;

// 1. 允许跨域，这样 Vue 前端才能访问这个后端
app.use(cors());
app.use(express.json());

/**
 * 核心接口：获取紫外线指数
 * 前端会发送: /api/uv?lat=-37.8&lon=144.9
 */
app.get('/api/uv', async (req, res) => {
    const { lat, lon } = req.query;

    if (!lat || !lon) {
        return res.status(400).json({ error: "Missing latitude or longitude" });
    }

    try {
        // 后端代替前端访问 Open-Meteo API
        const response = await axios.get(
            `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=uv_index`
        );

        // 获取紫外线数据
        const uvIndex = response.data.current.uv_index;

        // 返回给前端
        res.json({
            uv_index: uvIndex,
            source: "Backend Proxy",
            timestamp: new Date().toISOString()
        });

    } catch (error) {
        console.error("Error calling Open-Meteo:", error.message);
        res.status(500).json({ error: "Backend failed to fetch UV data" });
    }
});

app.listen(PORT, () => {
    console.log(`SunGuard Backend is running at http://localhost:${PORT}`);
});