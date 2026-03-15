<script setup>

defineProps({

icon:String,
title:String,
text:String

})

</script>

<template>

<div class="card">

<h3>{{icon}} {{title}}</h3>

<p>{{text}}</p>

</div>

</template>

<style scoped>

.card{

background:white;

color:black;

padding:20px;

margin:15px 0;

border-radius:10px;

}

</style>
