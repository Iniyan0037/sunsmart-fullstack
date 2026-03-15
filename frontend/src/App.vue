<script setup>
import BottomNav from "./components/BottomNav.vue"
</script>

<template>
  <div id="app">
    <main class="main-content">
      <router-view />
    </main>
    
    <BottomNav />
  </div>
</template>

<style>
/* --- Global Styles Reset --- */
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  display: block; 
}

/* --- Root Container Layout --- */
#app {
  font-family: Arial, Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  /* Force full viewport dimensions */
  width: 100vw;
  min-height: 100vh;
  margin: 0;
  padding: 0;

  /* Use Flexbox column to stack content and navigation */
  display: flex;
  flex-direction: column;
}

/* --- Centering Logic --- */
.main-content {
  /* Occupy all remaining space above the nav bar */
  flex: 1;
  width: 100%;
  
  /* Flexbox centering: perfectly aligns the router-view content */
  display: flex;
  justify-content: center; /* Horizontal centering */
  align-items: center;     /* Vertical centering */
  
  box-sizing: border-box;
}

/* --- Global Background Configuration --- */
body {
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* Ensure Nav bar doesn't shrink when content is large */
BottomNav {
  flex-shrink: 0;
}
</style>