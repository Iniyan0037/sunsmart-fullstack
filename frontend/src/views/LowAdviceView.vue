<template>

  <div class="page">

  <div class="container">

  <h1 class="title">Low UV Level</h1>

  <p class="subtitle">UV Index 0-2</p >

  <div class="status">
  🟢 Safe UV Level
  </div>

  <div class="grid">

  <div class="card">

  <div class="icon">😎</div>

  <h3>Sunglasses</h3>

  <p>Wear sunglasses on bright days</p >

  </div>

  <div class="card">

  <div class="icon">🧴</div>

  <h3>Sunscreen</h3>

  <p>Optional for long outdoor exposure</p >

  </div>

  <div class="card">

  <div class="icon">🏃</div>

  <h3>Outdoor Activity</h3>

  <p>Safe to enjoy outdoor activities</p >

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

  width:650px;
  max-width:95%;

  background:rgba(0,0,0,0.65);

  padding:45px;

  border-radius:22px;

  color:white;

  text-align:center;

  box-shadow:0 15px 45px rgba(0,0,0,0.4);
  }

  .title{
  font-size:36px;
  margin-bottom:5px;
  }

  .subtitle{
  opacity:0.8;
  margin-bottom:20px;
  }

  .status{
  background:#2ecc71;
  padding:10px 20px;
  border-radius:20px;
  display:inline-block;
  margin-bottom:30px;
  font-weight:bold;
  }

  .grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
  gap:18px;
  }

  .card{

  background:rgba(255,255,255,0.15);

  padding:20px;

  border-radius:16px;

  transition:0.2s;
  }

  .card:hover{
  background:rgba(255,255,255,0.3);
  transform:translateY(-4px);
  }

  .icon{
  font-size:36px;
  margin-bottom:10px;
  }

  h3{
  margin-bottom:6px;
  }

  p{
  font-size:14px;
  opacity:0.9;
  }

  </style>