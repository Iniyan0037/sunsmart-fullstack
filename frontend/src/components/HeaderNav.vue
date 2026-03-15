<template>

  <header class="header">

  <h2>SunSmart</h2>

  <nav>

  <router-link to="/dashboard">UV Level</router-link>

  <router-link to="/protection">Protection</router-link>

  <router-link to="/health">UV Risks</router-link>

  </nav>

  </header>

  </template>

  <style scoped>

  .header{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:20px;
  background:#f5f5f5;
  }

  nav a{
  margin-left:20px;
  text-decoration:none;
  font-weight:bold;
  }

  </style>
