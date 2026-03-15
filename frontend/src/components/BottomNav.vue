<template>

  <div class="nav">

  <router-link to="/">🏠 Home</router-link>

  <router-link to="/uv">☀ UV</router-link>

  <router-link to="/skin">🧑 Skin</router-link>

  <router-link to="/resources">📚 Learn</router-link>

  </div>

  </template>

  <style scoped>

  .nav{

  position:fixed;

  bottom:0;

  left:0;

  width:100%;

  height:70px;

  background:#1f1f1f;

  display:flex;

  justify-content:space-around;

  align-items:center;

  color:white;

  }

  a{

  color:white;

  text-decoration:none;

  font-size:16px;

  }

  .router-link-active{

  color:#4ecdc4;

  }

  </style>
