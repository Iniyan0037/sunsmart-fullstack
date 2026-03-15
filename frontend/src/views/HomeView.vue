<template>

  <div class="home">

  <div class="container">

  <div class="header">
  <span class="icon">🛡</span>
  <h1>SunGuard</h1>
  </div>

  <p class="intro">
  SunGuard helps you understand ultraviolet (UV) radiation and learn how to protect your skin from harmful sun exposure.
  </p >

  <div class="card">
  <h3>☀ UV Radiation</h3>
  <p>
  Ultraviolet radiation from the sun can damage skin cells and increase the risk of skin cancer.
  Understanding UV exposure is the first step to protecting your health.
  </p >
  </div>

  <div class="card">
  <h3>🧴 Sun Protection</h3>
  <p>
  Protect your skin by applying sunscreen, wearing protective clothing and using sunglasses during high UV periods.
  </p >
  </div>

  <div class="card">
  <h3>📊 UV Awareness</h3>
  <p>
  Monitoring the UV index helps you know when sun protection is necessary and when it is safer to stay in the shade.
  </p >
  </div>

  <p class="footer">
  Use the navigation bar below to explore UV levels, discover your skin type protection tips and learn more about sun safety.
  </p >

  </div>

  </div>

  </template>

  <style scoped>

  .home{
  width:100%;
  min-height:100vh;

  background:url("../assets/home.jpg") center center no-repeat;
  background-size:cover;

  display:flex;
  justify-content:center;
  align-items:center;

  padding:80px 20px;
  box-sizing:border-box;
  }

  .container{
  width:720px;
  max-width:92%;

  background:rgba(0,0,0,0.65);

  padding:40px;

  border-radius:18px;

  color:white;

  text-align:center;
  }

  .header{
  display:flex;
  justify-content:center;
  align-items:center;
  gap:10px;
  margin-bottom:10px;
  }

  .icon{
  font-size:34px;
  }

  h1{
  font-size:42px;
  margin:0;
  }

  .intro{
  margin-bottom:30px;
  line-height:1.6;
  }

  .card{
  background:rgba(255,255,255,0.15);
  padding:20px;
  border-radius:12px;
  margin-bottom:20px;
  }

  .footer{
  margin-top:20px;
  font-size:14px;
  opacity:0.9;
  }

  </style>