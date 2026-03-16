<template>
  <div class="page">
    <div class="container">
      <h1 class="title">🛡 SunGuard</h1>
      <h2 class="subtitle">Skin Cancer Research</h2>

      <p class="intro">
        Skin cancer is one of the most common cancers in Australia,
        strongly linked to UV radiation exposure.
      </p>

      <div class="card">
        <h3>Melanoma Incidence Rates in Australia (1968–2011)</h3>
        <p class="chart-desc">Age-standardised rates per 100,000 population by sex</p>
        <div class="chart-wrap">
          <canvas ref="cancerChart"></canvas>
        </div>
      </div>

      <div class="card">
        <h3>Average Temperature Trends by City (1995–2024)</h3>
        <p class="chart-desc">Annual average temperature across Australian capital cities</p>
        <div class="city-select">
          <label>Select city:</label>
          <select v-model="selectedCity" @change="loadTempChart">
            <option v-for="city in cities" :key="city" :value="city">{{ city }}</option>
          </select>
        </div>
        <div class="chart-wrap">
          <canvas ref="tempChart"></canvas>
        </div>
      </div>

      <div class="card">
        <h3>Key Statistics</h3>
        <table>
          <tr><th>Indicator</th><th>Value</th></tr>
          <tr><td>Lifetime risk</td><td>2 in 3 Australians</td></tr>
          <tr><td>Melanoma survival rate</td><td>~94%</td></tr>
          <tr><td>Skin cancers linked to UV exposure</td><td>~95%</td></tr>
          <tr><td>New melanoma cases each year</td><td>~15,000</td></tr>
          <tr><td>Annual deaths</td><td>~2,000</td></tr>
        </table>
      </div>

      <div class="card">
        <h3>🛡 Prevention Tips</h3>
        <ul>
          <li>Use sunscreen SPF 30+ regularly</li>
          <li>Wear protective clothing and hats</li>
          <li>Use sunglasses to protect eyes</li>
          <li>Seek shade during high UV periods</li>
          <li>Check the daily UV index before outdoor activities</li>
        </ul>
      </div>

      <div class="card resources">
        <h3>Learn More</h3>
        <div class="links">
          <button @click="openSunSmart">SunSmart Australia</button>
          <button @click="openCancer">Cancer Council</button>
          <button @click="openWHO">WHO UV Radiation</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { nextTick, onMounted, ref } from "vue"
import Chart from "chart.js/auto"
import { API_BASE } from "@/config"

const cancerChart = ref(null)
const tempChart = ref(null)
const selectedCity = ref("Melbourne")
const cities = ref([])
let cancerChartInstance = null
let tempChartInstance = null

async function loadCancerChart() {
  const res = await fetch(`${API_BASE}/api/cancer-stats`)
  if (!res.ok) {
    throw new Error("Failed to load cancer stats")
  }

  const data = await res.json()

  if (cancerChartInstance) {
    cancerChartInstance.destroy()
  }

  cancerChartInstance = new Chart(cancerChart.value, {
    type: "line",
    data: {
      labels: data.labels,
      datasets: data.datasets.map((d) => ({
        ...d,
        tension: 0.3,
        fill: true,
        pointRadius: 2,
        spanGaps: true,
      })),
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: "white" } },
        tooltip: { mode: "index", intersect: false },
      },
      scales: {
        x: {
          ticks: { color: "white" },
          grid: { color: "rgba(255,255,255,0.1)" },
        },
        y: {
          ticks: { color: "white" },
          grid: { color: "rgba(255,255,255,0.1)" },
          title: { display: true, text: "Rate per 100,000", color: "white" },
        },
      },
    },
  })
}

async function loadTempChart() {
  const res = await fetch(`${API_BASE}/api/uv-trends?city=${encodeURIComponent(selectedCity.value)}`)
  if (!res.ok) {
    throw new Error("Failed to load temperature chart")
  }

  const data = await res.json()
  cities.value = data.cities || []

  if (tempChartInstance) {
    tempChartInstance.destroy()
  }

  await nextTick()

  tempChartInstance = new Chart(tempChart.value, {
    type: "line",
    data: {
      labels: data.labels,
      datasets: data.datasets.map((d) => ({
        ...d,
        tension: 0.3,
        fill: true,
        pointRadius: 2,
        spanGaps: true,
      })),
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: "white" } },
      },
      scales: {
        x: {
          ticks: { color: "white" },
          grid: { color: "rgba(255,255,255,0.1)" },
        },
        y: {
          ticks: { color: "white" },
          grid: { color: "rgba(255,255,255,0.1)" },
          title: { display: true, text: "Avg Temperature (°C)", color: "white" },
        },
      },
    },
  })
}

function openSunSmart() {
  window.open("https://www.sunsmart.com.au", "_blank")
}

function openCancer() {
  window.open("https://www.cancer.org.au", "_blank")
}

function openWHO() {
  window.open("https://www.who.int", "_blank")
}

onMounted(async () => {
  try {
    await loadCancerChart()
    await loadTempChart()
  } catch (error) {
    console.error(error)
    alert("Failed to load research data")
  }
})
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
  background: rgba(0,0,0,0.70);
  padding: 40px;
  border-radius: 20px;
  color: white;
}
.title { text-align: center; font-size: 36px; margin-bottom: 5px; }
.subtitle { text-align: center; margin-bottom: 20px; }
.intro { text-align: center; margin-bottom: 30px; line-height: 1.6; }
.card {
  background: rgba(255,255,255,0.12);
  padding: 25px;
  border-radius: 14px;
  margin-bottom: 25px;
}
.chart-desc { font-size: 13px; opacity: 0.75; margin-bottom: 15px; }
.chart-wrap { position: relative; height: 300px; }
.city-select {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 15px;
}
.city-select select {
  padding: 6px 12px;
  border-radius: 8px;
  border: none;
  background: rgba(255,255,255,0.2);
  color: white;
  cursor: pointer;
}
.city-select select option {
  background: #333;
  color: white;
}
table { width: 100%; border-collapse: collapse; margin-top: 15px; }
th {
  text-align: left;
  padding: 10px;
  border-bottom: 1px solid rgba(255,255,255,0.3);
}
td {
  padding: 10px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
ul { padding-left: 20px; line-height: 1.7; }
.links { display: flex; gap: 10px; margin-top: 15px; flex-wrap: wrap; }
button {
  padding: 10px 18px;
  border: none;
  border-radius: 8px;
  background: #3498db;
  color: white;
  cursor: pointer;
}
button:hover { background: #2980b9; }
</style>
