<script setup>
import BottomNav from "./components/BottomNav.vue"
</script>

<template>
  <div id="app">
    <router-view />
    <BottomNav />
  </div>
</template>

<style>
html {
  overflow-x: hidden;
}

html, body, #app {
  margin: 0;
  padding: 0;
  width: 100%;
  min-height: 100vh;
  font-family: Arial, Helvetica, sans-serif;
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: border-box;
}

body {
  background: #111;
  background-size: cover;
  background-attachment: fixed;
  overflow-x: hidden;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
  max-width: 100vw;
  overflow-x: hidden;
}
</style>
