<template>
  <div class="page">
    <div class="container">
      <div class="header">
        <span class="icon">🛡</span>
        <h1>SunGuard</h1>
      </div>

      <h2 class="subtitle">UV Tracker</h2>

      <div class="location">
        <input v-model="postcode" placeholder="Enter Australian postcode" />
        <button @click="searchPostcode">Search</button>
        <button @click="getLocation">Use My Location</button>
      </div>

      <div v-if="uv !== null" class="uvCard">
        <h2>{{ location }}</h2>
        <div class="circle" :style="{ background: uvColor }">
          {{ uv }}
        </div>
        <p class="level">{{ level }}</p>
      </div>

      <div v-if="uv !== null" class="barSection">
        <div class="uvBar">
          <div class="marker" :style="{ left: markerPosition }"></div>
        </div>
        <div class="labels">
          <span class="low">Low</span>
          <span class="moderate">Moderate</span>
          <span class="high">High</span>
          <span class="veryhigh">Very High</span>
          <span class="extreme">Extreme</span>
        </div>
      </div>

      <div class="card advice" @click="goAdvice">
        <h3>Protection Advice</h3>
        <p>View recommended protection actions for different UV levels from Low to Extreme.</p>
      </div>

      <div class="card research" @click="goResearch">
        <h3>Skin Cancer Research</h3>
        <p>Explore statistics and insights about UV exposure and skin cancer risk in Australia.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

// State variables
const postcode = ref("");
const uv = ref(null);
const location = ref("Australia");
const level = ref("");
const uvColor = ref("#f1c40f");
const markerPosition = ref("20%");

// Navigation functions
function goAdvice() {
  router.push("/uv-advice");
}

function goResearch() {
  router.push("/research");
}

/**
 * Step 1: Search latitude/longitude via Postcode
 * (Keeping this simple via public API, or you can move to backend too)
 */
async function searchPostcode() {
  if (!postcode.value) return;

  try {
    const res = await fetch(`https://api.zippopotam.us/au/${postcode.value}`);
    if (!res.ok) {
      alert("Invalid Australian postcode");
      return;
    }

    const data = await res.json();
    const lat = data.places[0].latitude;
    const lon = data.places[0].longitude;
    location.value = data.places[0]["place name"];

    // Trigger UV fetch from OUR backend
    getUV(lat, lon);
  } catch (error) {
    console.error("Postcode search failed:", error);
    alert("Postcode search failed");
  }
}

/**
 * Step 2: Get browser geolocation
 */
function getLocation() {
  if (!navigator.geolocation) {
    alert("Geolocation is not supported by your browser");
    return;
  }

  navigator.geolocation.getCurrentPosition((pos) => {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;
    location.value = "Current Location";
    
    // Trigger UV fetch from OUR backend
    getUV(lat, lon);
  });
}

/**
 * Step 3: Fetch UV Index from YOUR BACKEND
 * This satisfies the requirement: "Not directly access the external API"
 */
async function getUV(lat, lon) {
  try {
    // 关键修改：请求地址指向你本地运行的 Node.js 后端
    const backendUrl = `http://3.107.240.160:3000/api/uv?lat=${lat}&lon=${lon}`;
    
    const res = await fetch(backendUrl);
    
    if (!res.ok) {
      throw new Error("Backend server error");
    }

    const data = await res.json();

    // 根据后端返回的数据结构更新（假设后端返回 { uv_index: 5.2 }）
    uv.value = parseFloat(data.uv_index).toFixed(1);

    // Update UI levels and colors
    setLevel();
  } catch (error) {
    console.error("Error fetching from backend:", error);
    alert("Failed to fetch UV data from backend server. Make sure your server.js is running!");
  }
}

/**
 * UI Logic: Determine UV Level and styling
 */
function setLevel() {
  if (uv.value <= 2) {
    level.value = "Low";
    uvColor.value = "#2ecc71";
    markerPosition.value = "5%";
  } else if (uv.value <= 5) {
    level.value = "Moderate";
    uvColor.value = "#f1c40f";
    markerPosition.value = "30%";
  } else if (uv.value <= 7) {
    level.value = "High";
    uvColor.value = "#e67e22";
    markerPosition.value = "50%";
  } else if (uv.value <= 10) {
    level.value = "Very High";
    uvColor.value = "#e74c3c";
    markerPosition.value = "75%";
  } else {
    level.value = "Extreme";
    uvColor.value = "#8e44ad";
    markerPosition.value = "95%";
  }
}
</script>

<style scoped>
/* 保持你原来的样式不变 */
.page {
  width: 100%;
  min-height: 100vh;
  background: url("../assets/uv.jpg") center center no-repeat;
  background-size: cover;
  display: flex;
  justify-content: center;
  padding: 80px 20px;
}

.container {
  width: 900px;
  max-width: 95%;
  background: rgba(0, 0, 0, 0.65);
  padding: 40px;
  border-radius: 20px;
  color: white;
}

.header {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.icon {
  font-size: 30px;
}

.subtitle {
  text-align: center;
  margin-bottom: 30px;
}

.location {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.location input {
  padding: 10px;
  border-radius: 8px;
  border: none;
  width: 200px;
}

.location button {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  background: #3498db;
  color: white;
  cursor: pointer;
}

.location button:hover {
  background: #2980b9;
}

.uvCard {
  text-align: center;
  margin-bottom: 30px;
}

.circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 36px;
  color: white;
  margin: 10px auto;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.level {
  font-size: 20px;
  font-weight: bold;
}

.barSection {
  margin-bottom: 40px;
  text-align: center;
}

.uvBar {
  height: 16px;
  background: linear-gradient(to right, #2ecc71, #f1c40f, #e67e22, #e74c3c, #8e44ad);
  border-radius: 10px;
  position: relative;
  margin-top: 10px;
}

.marker {
  width: 10px;
  height: 26px;
  background: white;
  position: absolute;
  top: -5px;
  border-radius: 2px;
  transition: 0.4s ease-out;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
}

.labels {
  display: flex;
  justify-content: space-between;
  margin-top: 8px;
  font-size: 13px;
}

.low { color: #2ecc71; }
.moderate { color: #f1c40f; }
.high { color: #e67e22; }
.veryhigh { color: #e74c3c; }
.extreme { color: #8e44ad; }

.card {
  background: rgba(255, 255, 255, 0.15);
  padding: 25px;
  border-radius: 12px;
  margin-bottom: 25px;
  cursor: pointer;
  transition: 0.3s;
}

.card:hover {
  background: rgba(255, 255, 255, 0.25);
  transform: translateY(-3px);
}
</style>