<template>

  <div class="page">

  <div class="container">

  <h1 class="title">SunGuard Learning Hub</h1>

  <p class="subtitle">
  Explore how sunlight and UV radiation affect your health.
  </p >

  <div class="grid">

  <div class="card" @click="goUV">
  <div class="icon">☀</div>
  <h3>UV Radiation</h3>
  <p>Learn about UVA, UVB and how UV damages skin.</p >
  </div>

  <div class="card" @click="goVitamin">
  <div class="icon">💊</div>
  <h3>Vitamin D</h3>
  <p>Understand how sunlight helps your body produce Vitamin D.</p >
  </div>

  <div class="card" @click="goCancer">
  <div class="icon">⚠</div>
  <h3>Skin Cancer</h3>
  <p>Discover the risks of UV exposure and prevention.</p >
  </div>

  <div class="card" @click="openSunSmart">
  <div class="icon">🌏</div>
  <h3>SunSmart Australia</h3>
  <p>Visit Australia's official sun safety resource.</p >
  </div>

  </div>

  </div>

  </div>

  </template>

  <script setup>

  import {useRouter} from "vue-router"

  const router = useRouter()

  function goUV(){
  router.push("/learn/uv")
  }

  function goVitamin(){
  router.push("/learn/vitamind")
  }

  function goCancer(){
  router.push("/learn/skincancer")
  }

  function openSunSmart(){
  window.open("https://www.sunsmart.com.au")
  }

  </script>

  <style scoped>

  .page{
  width:100%;
  min-height:100vh;
  background:url("../assets/sunprotect.jpg") center center no-repeat;
  background-size:cover;
  display:flex;
  justify-content:center;
  align-items:center;
  padding:60px;
  }

  .container{
  width:950px;
  background:rgba(0,0,0,0.65);
  padding:40px;
  border-radius:20px;
  color:white;
  text-align:center;
  }

  .grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:25px;
  }

  .card{
  background:rgba(255,255,255,0.12);
  padding:30px;
  border-radius:14px;
  cursor:pointer;
  transition:0.3s;
  }

  .card:hover{
  transform:translateY(-4px);
  background:rgba(255,255,255,0.25);
  }

  .icon{
  font-size:40px;
  margin-bottom:10px;
  }

  </style>
