<template>
  <div class="page">
    <div class="container">
      <h1 class="title">Clothing Recommendations</h1>
      <p class="intro">Find out what to wear based on the current UV index to protect your skin outdoors.</p>

      <div class="input-section">
        <input v-model="uvInput" type="number" min="0" max="20" step="0.1" placeholder="Enter UV index (e.g. 7.9)" />
        <button @click="getRecommendation">Get Recommendation</button>
        <button class="secondary" @click="useCurrentUV">Use Current UV</button>
      </div>

      <div v-if="result" class="result-card">
        <div class="uv-badge" :style="{ background: uvColor }">
          UV {{ result.uv_index }}
        </div>
        <p class="note">{{ result.note }}</p>
        <ul class="items">
          <li v-for="item in result.items" :key="item">
            {{ item }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue"
import { useRoute } from "vue-router"
import { API_BASE } from "@/config"

const uvInput = ref("")
const result = ref(null)
const route = useRoute()

onMounted(() => {
  if (route.query.uv) {
    uvInput.value = route.query.uv
    getRecommendation()
  }
})

const uvColor = computed(() => {
  const uv = parseFloat(uvInput.value)
  if (uv <= 2) return "#2ecc71"
  if (uv <= 5) return "#f1c40f"
  if (uv <= 7) return "#e67e22"
  if (uv <= 10) return "#e74c3c"
  return "#8e44ad"
})

async function getRecommendation() {
  if (!uvInput.value) return

  const res = await fetch(`${API_BASE}/api/clothing?uv=${uvInput.value}`)
  if (!res.ok) {
    alert("Failed to fetch recommendation")
    return
  }

  result.value = await res.json()
}

async function useCurrentUV() {
  navigator.geolocation.getCurrentPosition(async (pos) => {
    const lat = pos.coords.latitude
    const lon = pos.coords.longitude

    const res = await fetch(`${API_BASE}/api/uv?lat=${lat}&lon=${lon}`)
    if (!res.ok) {
      alert("Failed to fetch current UV")
      return
    }

    const data = await res.json()
    uvInput.value = data.uv_index
    getRecommendation()
  })
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
  align-items: center;
  padding: 80px 20px;
}
.container {
  width: 700px;
  max-width: 95%;
  background: rgba(0,0,0,0.70);
  padding: 40px;
  border-radius: 20px;
  color: white;
  text-align: center;
}
.title { font-size: 36px; margin-bottom: 10px; }
.intro { opacity: 0.85; margin-bottom: 30px; line-height: 1.6; }
.input-section {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 30px;
  flex-wrap: wrap;
}
.input-section input {
  padding: 10px 16px;
  border-radius: 8px;
  border: none;
  font-size: 15px;
  width: 220px;
}
.input-section button {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  background: #3498db;
  color: white;
  cursor: pointer;
  font-size: 15px;
}
.input-section button:hover { background: #2980b9; }
.input-section .secondary { background: #2ecc71; }
.input-section .secondary:hover { background: #27ae60; }
.result-card {
  background: rgba(255,255,255,0.12);
  padding: 30px;
  border-radius: 14px;
}
.uv-badge {
  display: inline-block;
  padding: 8px 24px;
  border-radius: 20px;
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 16px;
  color: white;
}
.note {
  font-size: 15px;
  margin-bottom: 20px;
  opacity: 0.9;
  line-height: 1.6;
}
.items {
  list-style: none;
  padding: 0;
  text-align: left;
  display: inline-block;
}
.items li {
  padding: 8px 0;
  font-size: 15px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
.items li:last-child { border-bottom: none; }
</style>
