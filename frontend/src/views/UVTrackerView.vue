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

      <div v-if="uvStore.uv !== null" class="uvCard">
        <h2>{{ uvStore.location }}</h2>
        <div class="circle" :style="{ background: uvStore.uvColor }">{{ uvStore.uv }}</div>
        <p class="level">{{ uvStore.level }}</p>
      </div>

      <div v-if="uvStore.uv !== null" class="barSection">
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
        <h3>Sunscreen Calculator</h3>
        <p>Get personalised sunscreen dosage based on your UV level.</p>
      </div>

      <div class="card" @click="router.push({ path: '/clothing', query: { uv: uvStore.uv } })">
        <h3>Clothing Guide</h3>
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

const router = useRouter()
const postcode = ref("")

async function searchPostcode() {
  if (!postcode.value) return
  try {
    const res = await fetch(`https://api.zippopotam.us/au/${postcode.value}`)
    if (!res.ok) { alert("Invalid Australian postcode"); return }
    const data = await res.json()
    uvStore.location = data.places[0]["place name"]
    getUV(data.places[0].latitude, data.places[0].longitude)
  } catch {
    alert("Postcode search failed")
  }
}

function getLocation() {
  navigator.geolocation.getCurrentPosition((pos) => {
    uvStore.location = "Current Location"
    getUV(pos.coords.latitude, pos.coords.longitude)
  })
}

async function getUV(lat, lon) {
  try {
    const res = await fetch(`/api/uv?lat=${lat}&lon=${lon}`)
    const data = await res.json()
    uvStore.uv = parseFloat(data.uv_index).toFixed(1)
    setLevel()
  } catch {
    alert("Failed to fetch UV data")
  }
}

function setLevel() {
  const val = parseFloat(uvStore.uv)
  if (val <= 2) { uvStore.level = "Low"; uvStore.uvColor = "#2ecc71"; uvStore.markerPosition = "5%" }
  else if (val <= 5) { uvStore.level = "Moderate"; uvStore.uvColor = "#f1c40f"; uvStore.markerPosition = "30%" }
  else if (val <= 7) { uvStore.level = "High"; uvStore.uvColor = "#e67e22"; uvStore.markerPosition = "50%" }
  else if (val <= 10) { uvStore.level = "Very High"; uvStore.uvColor = "#e74c3c"; uvStore.markerPosition = "75%" }
  else { uvStore.level = "Extreme"; uvStore.uvColor = "#8e44ad"; uvStore.markerPosition = "95%" }
}

function goAdvice() {
  const val = parseFloat(uvStore.uv)
  if (!val) return router.push("/uv-advice")
  if (val <= 2) router.push("/uv-advice/low")
  else if (val <= 5) router.push("/uv-advice/moderate")
  else if (val <= 7) router.push("/uv-advice/high")
  else if (val <= 10) router.push("/uv-advice/veryhigh")
  else router.push("/uv-advice/extreme")
}
</script>

<style scoped>
.page { width:100%; min-height:100vh; background:url("../assets/uv.jpg") center center no-repeat; background-size:cover; display:flex; justify-content:center; padding:80px 20px; }
.container { width:900px; max-width:95%; background:rgba(0,0,0,0.65); padding:40px; border-radius:20px; color:white; }
.header { display:flex; justify-content:center; align-items:center; gap:10px; }
.icon { font-size:30px; }
.subtitle { text-align:center; margin-bottom:30px; }
.location { display:flex; justify-content:center; gap:10px; margin-bottom:20px; }
.location input { padding:10px; border-radius:8px; border:none; }
.location button { padding:10px 20px; border:none; border-radius:8px; background:#3498db; color:white; cursor:pointer; }
.uvCard { text-align:center; margin-bottom:30px; }
.circle { width:120px; height:120px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:36px; color:white; margin:10px auto; }
.level { font-size:20px; }
.barSection { margin-bottom:40px; text-align:center; }
.uvBar { height:16px; background:linear-gradient(to right, #2ecc71, #f1c40f, #e67e22, #e74c3c, #8e44ad); border-radius:10px; position:relative; margin-top:10px; }
.marker { width:10px; height:26px; background:white; position:absolute; top:-5px; border-radius:2px; transition:0.4s; }
.labels { display:flex; justify-content:space-between; margin-top:8px; font-size:13px; }
.low{color:#2ecc71;} .moderate{color:#f1c40f;} .high{color:#e67e22;} .veryhigh{color:#e74c3c;} .extreme{color:#8e44ad;}
.card { background:rgba(255,255,255,0.15); padding:25px; border-radius:12px; margin-bottom:25px; cursor:pointer; }
.card:hover { background:rgba(255,255,255,0.25); }
</style>
