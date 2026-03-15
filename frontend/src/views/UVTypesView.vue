<template>

  <div class="page">

  <div class="container">

  <h1 class="title">☀ Understanding UV Radiation</h1>

  <p class="subtitle">
  Ultraviolet (UV) radiation from the sun affects our skin and health.
  Understanding different UV types helps us protect ourselves better.
  </p >


  <div class="grid">

  <div class="card uva">

  <div class="icon">☀</div>

  <h3>UVA Radiation</h3>

  <p>
  UVA rays penetrate deeply into the skin and contribute to premature aging,
  wrinkles and long-term skin damage. They are present all day and can pass
  through clouds and glass.
  </p >

  </div>


  <div class="card uvb">

  <div class="icon">🔥</div>

  <h3>UVB Radiation</h3>

  <p>
  UVB rays affect the outer skin layer and are the primary cause of sunburn.
  They also play a major role in the development of skin cancer.
  </p >

  </div>


  <div class="card uvc">

  <div class="icon">🛡</div>

  <h3>UVC Radiation</h3>

  <p>
  UVC radiation is extremely dangerous but is absorbed by the Earth's
  atmosphere and normally does not reach the surface.
  </p >

  </div>


  <div class="card tips">

  <div class="icon">🌤</div>

  <h3>UV Safety Tips</h3>

  <ul>

  <li>Check the UV index daily</li>
  <li>Use sunscreen SPF 30+</li>
  <li>Wear sunglasses and hats</li>
  <li>Seek shade during high UV periods</li>

  </ul>

  </div>

  </div>


  <div class="facts">

  <h2>Key Facts</h2>

  <ul>

  <li>Australia experiences some of the highest UV levels in the world</li>
  <li>UV radiation is the leading cause of skin cancer</li>
  <li>Protection is recommended when UV index reaches 3 or above</li>

  </ul>

  </div>


  <div class="external">

  <h2>Learn More</h2>

  <div class="links">

  <button @click="openWHO">WHO UV Radiation</button>

  <button @click="openCancer">Cancer Council</button>

  <button @click="openSunSmart">SunSmart Australia</button>

  </div>

  </div>

  </div>

  </div>

  </template>


  <script setup>

  function openWHO(){
  window.open("https://www.who.int/news-room/questions-and-answers/item/radiation-ultraviolet-(uv)")
  }

  function openCancer(){
  window.open("https://www.cancer.org.au")
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

  padding:80px 20px;

  }

  .container{

  width:1000px;

  background:rgba(0,0,0,0.65);

  padding:50px;

  border-radius:20px;

  color:white;

  }

  .title{

  text-align:center;

  font-size:40px;

  margin-bottom:10px;

  }

  .subtitle{

  text-align:center;

  margin-bottom:40px;

  opacity:0.9;

  }


  .grid{

  display:grid;

  grid-template-columns:1fr 1fr;

  gap:25px;

  margin-bottom:40px;

  }

  .card{

  background:rgba(255,255,255,0.12);

  padding:25px;

  border-radius:14px;

  transition:0.3s;

  }

  .card:hover{

  background:rgba(255,255,255,0.25);

  transform:translateY(-3px);

  }

  .icon{

  font-size:32px;

  margin-bottom:10px;

  }

  .card ul{

  padding-left:20px;

  }


  .facts{

  background:rgba(255,255,255,0.12);

  padding:25px;

  border-radius:14px;

  margin-bottom:35px;

  }

  .facts ul{

  padding-left:20px;

  }


  .external{

  text-align:center;

  }

  .links{

  display:flex;

  justify-content:center;

  gap:15px;

  margin-top:15px;

  }

  button{

  padding:12px 20px;

  border:none;

  border-radius:8px;

  background:#3498db;

  color:white;

  cursor:pointer;

  transition:0.2s;

  }

  button:hover{

  background:#2980b9;

  }

  </style>