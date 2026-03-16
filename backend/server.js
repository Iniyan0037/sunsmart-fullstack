const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors({
  origin: "https://sunsmart-frontend.onrender.com"
}));
app.use(express.json());

app.get("/", (req, res) => {
  res.send("SunSmart backend is running");
});

app.get("/api/uv", async (req, res) => {
  const lat = Number(req.query.lat);
  const lon = Number(req.query.lon);

  if (!Number.isFinite(lat) || lat < -90 || lat > 90) {
    return res.status(400).json({ error: "Invalid latitude" });
  }

  if (!Number.isFinite(lon) || lon < -180 || lon > 180) {
    return res.status(400).json({ error: "Invalid longitude" });
  }

  try {
    const response = await axios.get(
      `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=uv_index`
    );

    const uvIndex = response.data?.current?.uv_index;

    res.json({
      uv_index: uvIndex,
      source: "Backend Proxy",
      timestamp: new Date().toISOString(),
    });
  } catch (error) {
    console.error("Error calling Open-Meteo:", error.message);
    res.status(500).json({ error: "Backend failed to fetch UV data" });
  }
});

app.listen(PORT, () => {
  console.log(`SunSmart backend is running on port ${PORT}`);
});
