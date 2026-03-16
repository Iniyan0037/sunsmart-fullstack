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

const API_BASE = import.meta.env.VITE_API_BASE;
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

    getUV(lat, lon);
  });
}

/**
 * Step 3: Fetch UV Index from backend
 */
async function getUV(lat, lon) {
  try {
    const backendUrl = `${API_BASE}/api/uv?lat=${lat}&lon=${lon}`;
    const res = await fetch(backendUrl);

    if (!res.ok) {
      throw new Error("Backend server error");
    }

    const data = await res.json();
    uv.value = parseFloat(data.uv_index).toFixed(1);
    setLevel();
  } catch (error) {
    console.error("Error fetching from backend:", error);
    alert("Failed to fetch UV data from backend server.");
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
  padding: 12px;
  width: 250px;
  border-radius: 10px;
  border: none;
  outline: none;
  font-size: 16px;
}

.location button {
  padding: 12px 20px;
  border: none;
  border-radius: 10px;
  background: #3498db;
  color: white;
  font-weight: bold;
  cursor: pointer;
}

.location button:hover {
  background: #2980b9;
}

.uvCard {
  text-align: center;
  margin: 30px 0;
}

.circle {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  margin: 20px auto;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 42px;
  font-weight: bold;
  color: white;
}

.level {
  font-size: 22px;
  font-weight: bold;
}

.barSection {
  margin: 30px 0;
}

.uvBar {
  height: 14px;
  border-radius: 10px;
  background: linear-gradient(
    to right,
    #2ecc71 0%,
    #f1c40f 25%,
    #e67e22 50%,
    #e74c3c 75%,
    #8e44ad 100%
  );
  position: relative;
}

.marker {
  position: absolute;
  top: -6px;
  width: 4px;
  height: 26px;
  background: white;
  border-radius: 4px;
}

.labels {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
  font-size: 14px;
  font-weight: bold;
}

.card {
  margin-top: 25px;
  padding: 20px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.15);
  cursor: pointer;
  transition: 0.3s;
}

.card:hover {
  background: rgba(255, 255, 255, 0.25);
}

.card h3 {
  margin-bottom: 10px;
}
</style>
