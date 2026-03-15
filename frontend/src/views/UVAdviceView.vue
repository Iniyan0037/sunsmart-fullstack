<template>

  <div class="page">

  <div class="container">

  <h1>UV Protection Advice</h1>

  <div class="grid">

  <div class="card" @click="$router.push('/uv-advice/low')">
  🟢
  <h3>Low</h3>
  <p>0-2</p >
  </div>

  <div class="card" @click="$router.push('/uv-advice/moderate')">
  🟡
  <h3>Moderate</h3>
  <p>3-5</p >
  </div>

  <div class="card" @click="$router.push('/uv-advice/high')">
  🟠
  <h3>High</h3>
  <p>6-7</p >
  </div>

  <div class="card" @click="$router.push('/uv-advice/veryhigh')">
  🔴
  <h3>Very High</h3>
  <p>8-10</p >
  </div>

  <div class="card" @click="$router.push('/uv-advice/extreme')">
  🟣
  <h3>Extreme</h3>
  <p>11+</p >
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
  }

  .container{
  width:900px;
  background:rgba(0,0,0,0.65);
  padding:40px;
  border-radius:18px;
  color:white;
  text-align:center;
  }

  .grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
  gap:20px;
  margin-top:30px;
  }

  .card{
  background:rgba(255,255,255,0.15);
  padding:25px;
  border-radius:14px;
  cursor:pointer;
  font-size:24px;
  }

  </style>
