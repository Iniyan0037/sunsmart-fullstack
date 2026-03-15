<template>

  <div class="page">
  <div class="container">

  <h1 class="title">Skin Type III</h1>
  <p class="subtitle">Light Skin</p >

  <div class="tone"></div>

  <div class="section">
  <h3>☀ Protection</h3>
  <p>
  Light skin can tan gradually but may still burn under strong UV.
  Sun protection is recommended when UV index exceeds 4.
  </p >
  </div>

  <div class="section">
  <h3>🧴 Sunscreen</h3>
  <ul>
  <li>SPF 30+ sunscreen recommended</li>
  <li>Reapply after swimming or sweating</li>
  <li>Use protective clothing outdoors</li>
  </ul>
  </div>

  <div class="section">
  <h3>💊 Vitamin D</h3>
  <p>
  Moderate sunlight exposure helps maintain healthy Vitamin D levels.
  Avoid long exposure during peak UV hours.
  </p >
  </div>

  <div class="section">
  <h3>⚠ Health Risk</h3>
  <p>
  Moderate risk of sunburn and UV damage.
  Regular sun protection can significantly reduce long-term skin damage.
  </p >
  </div>

  </div>
  </div>

  </template>

  <style scoped>

  .page{
  width:100%;
  min-height:100vh;
  background:url("../assets/skin.jpg") center center no-repeat;
  background-size:cover;
  display:flex;
  justify-content:center;
  align-items:center;
  padding:60px 20px;
  }

  .container{
  width:700px;
  background:rgba(0,0,0,0.65);
  padding:40px;
  border-radius:18px;
  color:white;
  backdrop-filter:blur(10px);
  overflow-y:auto;
  max-height:85vh;
  }

  .title{text-align:center;font-size:36px;}
  .subtitle{text-align:center;margin-bottom:25px;}

  .tone{
  width:90px;
  height:90px;
  border-radius:50%;
  margin:0 auto 30px auto;
  background:#d9a47a;
  border:4px solid white;
  }

  .section{
  background:rgba(255,255,255,0.12);
  padding:22px;
  border-radius:12px;
  margin-bottom:20px;
  transition:0.3s;
  }

  .section:hover{
  background:rgba(255,255,255,0.22);
  transform:translateY(-2px);
  }

  </style>
