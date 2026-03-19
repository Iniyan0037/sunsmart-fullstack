<template>
  <div class="page">
    <div class="container">
      <div class="header">
        <span class="icon">🛡</span>
        <h1>SunGuard</h1>
      </div>
      <h2 class="subtitle">UV Tracker</h2>

      <div class="location">
        <div class="search-wrapper">
          <input
            v-model="searchQuery"
            placeholder="Enter suburb, city or postcode"
            @input="onInput"
            @keyup.enter="handleEnter"
            autocomplete="off"
          />
          <ul v-if="suggestions.length > 0" class="suggestions">
            <li
              v-for="s in suggestions"
              :key="`${s.name}-${s.state}-${s.lat}-${s.lon}`"
              @click="selectSuggestion(s)"
            >
              {{ s.name }}, {{ s.state }}
            </li>
          </ul>
        </div>
        <button @click="handleEnter">Search</button>
        <button @click="getLocation">Use My Location</button>
      </div>

      <div v-if="uvStore.fetched" class="uvCard">
        <h2>{{ uvStore.location }}</h2>
        <div class="circle" :style="{ background: uvStore.uvColor }">
          {{ uvStore.uv }}
        </div>
        <p class="level">{{ uvStore.level }}</p>
      </div>

      <div v-if="uvStore.fetched" class="barSection">
        <div class="uvBar">
          <div class="marker" :style="{ left: uvStore.markerPosition }"></div>
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

      <div class="card" @click="router.push({ path: '/sunscreen', query: { uv: uvStore.uv } })">
        <h3>🧴 Sunscreen Calculator</h3>
        <p>Get personalised sunscreen dosage based on your UV level.</p>
      </div>

      <div class="card" @click="router.push({ path: '/clothing', query: { uv: uvStore.uv } })">
        <h3>👕 Clothing Guide</h3>
        <p>Find out what to wear to protect your skin outdoors.</p>
      </div>

      <div class="card research" @click="router.push('/research')">
        <h3>Skin Cancer Research</h3>
        <p>Explore statistics and insights about UV exposure and skin cancer risk in Australia.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import { uvStore } from "@/store/uvStore"
import { API_BASE } from "@/config"

const router = useRouter()
const searchQuery = ref("")
const suggestions = ref([])
const selectedLat = ref(null)
const selectedLon = ref(null)

let debounceTimer = null

async function onInput() {
  const q = searchQuery.value.trim()
  selectedLat.value = null
  selectedLon.value = null

  if (q.length < 2) {
    suggestions.value = []
    return
  }

  if (/^\d+$/.test(q)) {
    suggestions.value = []
    return
  }

  clearTimeout(debounceTimer)
  debounceTimer = setTimeout(async () => {
    try {
      const res = await fetch(
        `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(q)}&countrycodes=au&format=json&limit=6&addressdetails=1`,
        { headers: { "Accept-Language": "en" } },
      )
      const data = await res.json()
      suggestions.value = data
        .map((item) => ({
          name:
            item.address?.suburb ||
            item.address?.city ||
            item.address?.town ||
            item.address?.village ||
            item.name,
          state: item.address?.state || "Australia",
          lat: parseFloat(item.lat),
          lon: parseFloat(item.lon),
        }))
        .filter((s) => s.name && Number.isFinite(s.lat) && Number.isFinite(s.lon))
    } catch {
      suggestions.value = []
    }
  }, 350)
}

function selectSuggestion(s) {
  searchQuery.value = `${s.name}, ${s.state}`
  selectedLat.value = s.lat
  selectedLon.value = s.lon
  suggestions.value = []
  uvStore.location = s.name
  getUV(s.lat, s.lon)
}

async function handleEnter() {
  suggestions.value = []
  const q = searchQuery.value.trim()
  if (!q) return

  if (selectedLat.value !== null && selectedLon.value !== null) {
    await getUV(selectedLat.value, selectedLon.value)
    return
  }

  if (/^\d+$/.test(q)) {
    try {
      const res = await fetch(`https://api.zippopotam.us/au/${q}`)
      if (!res.ok) {
        alert("Invalid Australian postcode")
        return
      }
      const data = await res.json()
      uvStore.location = data.places[0]["place name"]
      await getUV(data.places[0].latitude, data.places[0].longitude)
    } catch {
      alert("Postcode search failed")
    }
    return
  }

  try {
    const res = await fetch(
      `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(q)}&countrycodes=au&format=json&limit=1&addressdetails=1`,
      { headers: { "Accept-Language": "en" } },
    )
    const data = await res.json()
    if (!data.length) {
      alert("Location not found. Try a suburb or postcode.")
      return
    }
    const place = data[0]
    uvStore.location =
      place.address?.suburb ||
      place.address?.city ||
      place.address?.town ||
      place.address?.village ||
      place.name ||
      "Selected Location"
    await getUV(parseFloat(place.lat), parseFloat(place.lon))
  } catch {
    alert("Location search failed")
  }
}

function getLocation() {
  navigator.geolocation.getCurrentPosition(
    async (pos) => {
      uvStore.location = "Current Location"
      await getUV(pos.coords.latitude, pos.coords.longitude)
    },
    () => {
      alert("Unable to retrieve your location")
    },
  )
}

async function getUV(lat, lon) {
  try {
    const res = await fetch(`${API_BASE}/api/uv?lat=${lat}&lon=${lon}`)
    if (!res.ok) {
      throw new Error("Failed to fetch UV data")
    }

    const data = await res.json()
    uvStore.uv = parseFloat(data.uv_index).toFixed(1)
    uvStore.fetched = true
    setLevel()
  } catch {
    alert("Failed to fetch UV data")
  }
}

function setLevel() {
  const val = parseFloat(uvStore.uv)

  if (val <= 2) {
    uvStore.level = "Low"
    uvStore.uvColor = "#2ecc71"
    uvStore.markerPosition = "5%"
  } else if (val <= 5) {
    uvStore.level = "Moderate"
    uvStore.uvColor = "#f1c40f"
    uvStore.markerPosition = "30%"
  } else if (val <= 7) {
    uvStore.level = "High"
    uvStore.uvColor = "#e67e22"
    uvStore.markerPosition = "50%"
  } else if (val <= 10) {
    uvStore.level = "Very High"
    uvStore.uvColor = "#e74c3c"
    uvStore.markerPosition = "75%"
  } else {
    uvStore.level = "Extreme"
    uvStore.uvColor = "#8e44ad"
    uvStore.markerPosition = "95%"
  }
}

function goAdvice() {
  const val = parseFloat(uvStore.uv)

  if (Number.isNaN(val)) {
    router.push("/uv-advice")
    return
  }

  if (val <= 2) router.push("/uv-advice/low")
  else if (val <= 5) router.push("/uv-advice/moderate")
  else if (val <= 7) router.push("/uv-advice/high")
  else if (val <= 10) router.push("/uv-advice/veryhigh")
  else router.push("/uv-advice/extreme")
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
  padding: 80px 20px 100px;
}

.container {
  width: 100%;
  max-width: 900px;
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
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.search-wrapper {
  position: relative;
  width: 300px;
}

.search-wrapper input {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  border: none;
  font-size: 15px;
}

.suggestions {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: white;
  color: black;
  border-radius: 0 0 8px 8px;
  list-style: none;
  margin: 0;
  padding: 0;
  z-index: 100;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  max-height: 220px;
  overflow-y: auto;
}

.suggestions li {
  padding: 10px 14px;
  cursor: pointer;
  font-size: 14px;
  border-bottom: 1px solid #eee;
}

.suggestions li:hover {
  background: #f0f0f0;
}

.location button {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  background: #3498db;
  color: white;
  cursor: pointer;
  font-size: 15px;
  white-space: nowrap;
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
}

.level {
  font-size: 20px;
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
  transition: 0.4s;
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
}

.card:hover {
  background: rgba(255, 255, 255, 0.25);
}

@media (max-width: 600px) {
  .container {
    padding: 24px 16px;
  }

  .search-wrapper {
    width: 100%;
  }

  .location {
    flex-direction: column;
    align-items: center;
  }

  .location button {
    width: 100%;
  }
}
</style>
