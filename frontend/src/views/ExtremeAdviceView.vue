<template>

  <div class="page">

  <div class="container">

  <h1 class="title">Extreme UV Level</h1>
  <p class="subtitle">UV Index 11+</p >

  <div class="badge extreme">🟣 Extreme Risk</div>

  <div class="grid">

  <div class="card">
  <div class="icon">🚫☀</div>
  <h3>Avoid Sun</h3>
  <p>Stay indoors during midday</p >
  </div>

  <div class="card">
  <div class="icon">🧴</div>
  <h3>Maximum Sunscreen</h3>
  <p>Use SPF50+ sunscreen</p >
  </div>

  <div class="card">
  <div class="icon">🧢</div>
  <h3>Full Protection</h3>
  <p>Hat, sunglasses and clothing</p >
  </div>

  </div>

  </div>

  </div>

  </template>

  <style scoped>

  .page{
  width:100%;
  min-height:100vh;
  background:url("../assets/uv.jpg") center center no-repeat;
  background-size:cover;
  display:flex;
  justify-content:center;
  align-items:center;
  padding:60px 20px;
  }

  .container{
  width:720px;
  max-width:95%;
  background:rgba(0,0,0,0.65);
  padding:40px;
  border-radius:18px;
  color:white;
  text-align:center;
  }

  .title{font-size:42px;margin-bottom:6px;}

  .subtitle{
  opacity:0.8;
  margin-bottom:20px;
  }

  .badge{
  display:inline-block;
  padding:12px 28px;
  border-radius:25px;
  font-weight:bold;
  margin-bottom:30px;
  }

  .extreme{
  background:#8e44ad;
  }

  .grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:20px;
  }

  .card{
  background:rgba(255,255,255,0.2);
  padding:24px;
  border-radius:16px;
  }

  .icon{
  font-size:40px;
  margin-bottom:10px;
  }

  </style>