<template>
  <div class="page">
    <div class="container">
      <h1 class="title">Sunscreen Guide</h1>
      <p class="intro">Enter the current UV index to get your personalised sunscreen dosage recommendation.</p>

      <div class="input-section">
        <input v-model="uvInput" type="number" min="0" max="20" step="0.1" placeholder="Enter UV index (e.g. 7.9)" />
        <button @click="getRecommendation">Get Recommendation</button>
        <button class="secondary" @click="useCurrentUV">Use Current UV</button>
      </div>

      <div v-if="result" class="result-grid">
        <div class="stat-card">
          <div class="stat-value">{{ result.recommended_spf }}</div>
          <div class="stat-label">Recommended SPF</div>
        </div>

        <div class="stat-card">
          <div class="stat-value">{{ result.face_teaspoons }} tsp</div>
          <div class="stat-label">Face & Neck</div>
        </div>

        <div class="stat-card">
          <div class="stat-value">{{ result.body_teaspoons }} tsp</div>
          <div class="stat-label">Full Body</div>
        </div>

        <div class="stat-card highlight">
          <div class="stat-value">{{ result.reapply_minutes }} min</div>
          <div class="stat-label">Reapply Every</div>
        </div>
      </div>

      <div v-if="result" class="note-card">
        <p>{{ result.note }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import { API_BASE } from "@/config"

const route = useRoute()
const uvInput = ref("")
const result = ref(null)

onMounted(() => {
  if (route.query.uv) {
    uvInput.value = route.query.uv
    getRecommendation()
  }
})

async function getRecommendation() {
  if (!uvInput.value) return

  const res = await fetch(`${API_BASE}/api/sunscreen?uv=${uvInput.value}`)
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
  background: url("../assets/sunprotect.jpg") center center no-repeat;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 80px 20px;
}
.container {
  width: 800px;
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
.result-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 20px;
  margin-bottom: 20px;
}
.stat-card {
  background: rgba(255,255,255,0.12);
  padding: 24px 16px;
  border-radius: 14px;
}
.stat-card.highlight { background: rgba(52,152,219,0.35); }
.stat-value { font-size: 28px; font-weight: bold; margin-bottom: 6px; }
.stat-label { font-size: 13px; opacity: 0.8; }
.note-card {
  background: rgba(255,255,255,0.1);
  padding: 16px 24px;
  border-radius: 12px;
  font-size: 15px;
  line-height: 1.6;
}
</style>
