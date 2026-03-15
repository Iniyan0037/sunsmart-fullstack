<template>

  <div class="page">

  <div class="container">

  <h1 class="title">🛡 SunGuard</h1>

  <h2 class="subtitle">Skin Cancer Research</h2>

  <p class="intro">
  Skin cancer is one of the most common cancers in Australia and is strongly linked to ultraviolet (UV) radiation exposure.
  Understanding the risks and prevention methods can help reduce the chances of developing skin cancer.
  </p >


  <div class="card">

  <h3>⚠ Overview</h3>

  <p>
  Skin cancer occurs when ultraviolet radiation damages the DNA of skin cells. Over time, this damage can lead to uncontrolled
  cell growth and the development of cancer. Australia experiences extremely high UV levels, making sun protection
  especially important.
  </p >

  </div>


  <div class="card">

  <h3>📊 Skin Cancer Statistics (Australia)</h3>

  <table>

  <tr>
  <th>Indicator</th>
  <th>Value</th>
  </tr>

  <tr>
  <td>Lifetime risk</td>
  <td>66% (2 in 3 Australians)</td>
  </tr>

  <tr>
  <td>Melanoma survival rate</td>
  <td>94%</td>
  </tr>

  <tr>
  <td>Skin cancers caused by UV</td>
  <td>95%</td>
  </tr>

  <tr>
  <td>New melanoma cases each year</td>
  <td>~15,000</td>
  </tr>

  <tr>
  <td>Annual deaths</td>
  <td>~2,000</td>
  </tr>

  </table>

  </div>


  <div class="card">

  <h3>🧬 Types of Skin Cancer</h3>

  <table>

  <tr>
  <th>Type</th>
  <th>Percentage</th>
  <th>Description</th>
  </tr>

  <tr>
  <td>Basal Cell Carcinoma</td>
  <td>70%</td>
  <td>Most common and slow growing</td>
  </tr>

  <tr>
  <td>Squamous Cell Carcinoma</td>
  <td>25%</td>
  <td>Can spread if untreated</td>
  </tr>

  <tr>
  <td>Melanoma</td>
  <td>5%</td>
  <td>Most dangerous form</td>
  </tr>

  </table>

  </div>


  <div class="card">

  <h3>🛡 Prevention Tips</h3>

  <ul>

  <li>Use sunscreen SPF 30+ regularly</li>

  <li>Wear protective clothing and hats</li>

  <li>Use sunglasses to protect eyes</li>

  <li>Seek shade during high UV periods</li>

  <li>Check the daily UV index before outdoor activities</li>

  </ul>

  </div>


  <div class="card resources">

  <h3>🌏 Learn More</h3>

  <p>Explore trusted sources for more information:</p >

  <div class="links">

  <button @click="openSunSmart">SunSmart Australia</button>

  <button @click="openCancer">Cancer Council</button>

  <button @click="openWHO">WHO UV Radiation</button>

  </div>

  </div>


  </div>

  </div>

  </template>


  <script setup>

  function openSunSmart(){
  window.open("https://www.sunsmart.com.au")
  }

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

  background:url("../assets/uv.jpg") center center no-repeat;
  background-size:cover;

  display:flex;
  justify-content:center;

  padding:80px 20px;

  }

  .container{

  width:900px;
  max-width:95%;

  background:rgba(0,0,0,0.65);

  padding:40px;

  border-radius:20px;

  color:white;

  }

  .title{

  text-align:center;
  font-size:36px;

  margin-bottom:5px;

  }

  .subtitle{

  text-align:center;

  margin-bottom:20px;

  }

  .intro{

  text-align:center;

  margin-bottom:30px;

  line-height:1.6;

  }


  .card{

  background:rgba(255,255,255,0.12);

  padding:25px;

  border-radius:14px;

  margin-bottom:25px;

  transition:0.3s;

  }

  .card:hover{

  background:rgba(255,255,255,0.22);

  transform:translateY(-3px);

  }


  table{

  width:100%;

  border-collapse:collapse;

  margin-top:15px;

  }

  th{

  text-align:left;

  padding:10px;

  border-bottom:1px solid rgba(255,255,255,0.3);

  }

  td{

  padding:10px;

  border-bottom:1px solid rgba(255,255,255,0.1);

  }


  ul{

  padding-left:20px;

  line-height:1.7;

  }


  .links{

  display:flex;

  gap:10px;

  margin-top:15px;

  }

  button{

  padding:10px 18px;

  border:none;

  border-radius:8px;

  background:#3498db;

  color:white;

  cursor:pointer;

  }

  button:hover{

  background:#2980b9;

  }

  </style>
