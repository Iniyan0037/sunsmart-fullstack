<template>

  <div class="page">

  <div class="container">

  <h1>Vitamin D and Sunlight</h1>

  <div class="grid">

  <div class="card">

  <div class="icon">💊</div>

  <h3>Why Vitamin D Matters</h3>

  <p>
  Vitamin D supports bone health, immune function and muscle strength.
  </p >

  </div>


  <div class="card">

  <div class="icon">☀</div>

  <h3>Sunlight Production</h3>

  <p>
  Your skin produces Vitamin D when exposed to sunlight.
  Short exposure can be beneficial.
  </p >

  </div>


  <div class="card">

  <div class="icon">⚖</div>

  <h3>Healthy Balance</h3>

  <p>
  Too much sun exposure increases skin damage risk.
  Balance sunlight with sun protection.
  </p >

  </div>


  <div class="card">

  <div class="icon">🥛</div>

  <h3>Food Sources</h3>

  <p>
  Vitamin D can also be obtained from fish, eggs,
  fortified milk and supplements.
  </p >

  </div>

  </div>


  <div class="links">

  <button @click="openHealth">Health Australia</button>

  <button @click="openWHO">WHO Nutrition</button>

  </div>

  </div>

  </div>

  </template>

  <script setup>

  function openHealth(){
  window.open("https://www.health.gov.au")
  }

  function openWHO(){
  window.open("https://www.who.int")
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
  padding:80px;
  }

  .container{
  width:900px;
  background:rgba(0,0,0,0.65);
  padding:40px;
  border-radius:18px;
  color:white;
  }

  .grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:25px;
  margin-bottom:30px;
  }

  .card{
  background:rgba(255,255,255,0.12);
  padding:25px;
  border-radius:12px;
  }

  .icon{
  font-size:28px;
  margin-bottom:10px;
  }

  .links{
  text-align:center;
  }

  button{
  padding:12px 22px;
  border:none;
  border-radius:8px;
  background:#3498db;
  color:white;
  margin:5px;
  cursor:pointer;
  }

  </style>
