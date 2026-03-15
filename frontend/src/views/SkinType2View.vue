<template>

  <div class="page">

  <div class="container">

  <h1 class="title">Skin Type II</h1>
  <p class="subtitle">Fair Skin</p >

  <div class="tone"></div>

  <div class="section">
  <h3>☀ Protection</h3>
  <p>
  Fair skin burns easily under moderate UV exposure.
  Sun protection should be used when UV index reaches 3 or above.
  </p >
  </div>

  <div class="section">
  <h3>🧴 Sunscreen</h3>
  <ul>
  <li>Use SPF 50 sunscreen outdoors</li>
  <li>Reapply every 2 hours</li>
  <li>Wear sunglasses and a wide-brim hat</li>
  </ul>
  </div>

  <div class="section">
  <h3>💊 Vitamin D</h3>
  <p>
  Short daily sun exposure can help maintain Vitamin D levels.
  Always balance sun exposure with proper protection.
  </p >
  </div>

  <div class="section">
  <h3>⚠ Health Risk</h3>
  <p>
  Moderate risk of sunburn and long-term UV damage.
  Frequent sun exposure without protection may increase skin cancer risk.
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
  background:#f2d3b3;
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
