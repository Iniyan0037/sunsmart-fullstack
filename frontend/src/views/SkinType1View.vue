<template>

  <div class="page">

  <div class="container">

  <h1 class="title">Skin Type I</h1>
  <p class="subtitle">Very Fair Skin</p >


  <div class="tone"></div>


  <div class="section">

  <h3>☀ Protection</h3>

  <p>
  Very fair skin burns quickly under UV exposure.
  Strong sun protection is recommended when UV levels are moderate or higher.
  </p >

  </div>


  <div class="section">

  <h3>🧴 Sunscreen</h3>

  <ul>

  <li>Use SPF 50+ sunscreen</li>
  <li>Reapply every 2 hours outdoors</li>
  <li>Apply 20 minutes before sun exposure</li>

  </ul>

  </div>


  <div class="section">

  <h3>💊 Vitamin D</h3>

  <p>

  Short periods of sunlight exposure can help maintain Vitamin D levels.
  However excessive sun exposure should always be avoided.

  </p >

  </div>


  <div class="section">

  <h3>⚠ Health Risk</h3>

  <p>

  This skin type has the highest risk of sunburn and skin cancer.
  Protective clothing, hats and sunglasses are strongly recommended.

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

  .title{

  text-align:center;

  font-size:36px;

  }

  .subtitle{

  text-align:center;

  margin-bottom:25px;

  opacity:0.9;

  }

  .tone{

  width:90px;
  height:90px;

  border-radius:50%;

  margin:0 auto 30px auto;

  background:#f8e5d8;

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

  .section h3{

  margin-bottom:10px;

  }

  .section ul{

  padding-left:20px;

  }

  </style>