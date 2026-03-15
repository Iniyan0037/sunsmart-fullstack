<template>

  <div class="page">

  <div class="container">

  <h1>Skin Cancer Awareness</h1>

  <div class="grid">

  <div class="card">

  <div class="icon">⚠</div>

  <h3>Risk</h3>

  <p>
  Excessive UV radiation damages skin cells and increases
  the risk of melanoma and other skin cancers.
  </p >

  </div>


  <div class="card">

  <div class="icon">📊</div>

  <h3>Statistics</h3>

  <p>
  Australia has one of the highest skin cancer rates in the world.
  2 in 3 Australians will develop skin cancer before age 70.
  </p >

  </div>


  <div class="card">

  <div class="icon">🛡</div>

  <h3>Prevention</h3>

  <ul>

  <li>Use sunscreen SPF 30+</li>
  <li>Wear protective clothing</li>
  <li>Check UV index daily</li>
  <li>Seek shade during peak UV hours</li>

  </ul>

  </div>


  <div class="card">

  <div class="icon">🔍</div>

  <h3>Early Detection</h3>

  <p>
  Regular skin checks help detect skin cancer early
  and improve treatment outcomes.
  </p >

  </div>

  </div>


  <div class="links">

  <button @click="openCancer">Cancer Council</button>

  <button @click="openWHO">WHO Skin Cancer</button>

  </div>

  </div>

  </div>

  </template>

  <script setup>

  function openCancer(){
  window.open("https://www.cancer.org.au")
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
  background:#e74c3c;
  color:white;
  margin:5px;
  cursor:pointer;
  }

  </style>