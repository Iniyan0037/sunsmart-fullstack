<template>

  <div class="page">

  <div class="container">

  <h1 class="title">Skin Type V</h1>
  <p class="subtitle">Tan Skin</p >

  <div class="tone"></div>

  <div class="section">

  <h3>☀ Protection</h3>

  <p>
  Tan skin has stronger natural protection against UV radiation,
  but prolonged sun exposure can still damage skin cells.
  Sun protection is recommended during high UV levels.
  </p >

  </div>


  <div class="section">

  <h3>🧴 Sunscreen</h3>

  <ul>

  <li>SPF 15–30 sunscreen recommended</li>
  <li>Apply sunscreen before long sun exposure</li>
  <li>Wear sunglasses to protect eyes from UV radiation</li>

  </ul>

  </div>


  <div class="section">

  <h3>💊 Vitamin D</h3>

  <p>
  Regular short sun exposure helps maintain Vitamin D levels.
  People with darker skin may require slightly longer exposure to produce Vitamin D.
  </p >

  </div>


  <div class="section">

  <h3>⚠ Health Risk</h3>

  <p>
  Lower risk of sunburn compared to lighter skin types,
  but UV radiation can still contribute to skin aging and skin cancer risk.
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
  }

  .tone{
  width:90px;
  height:90px;

  border-radius:50%;

  margin:0 auto 30px auto;

  background:#8d5524;

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