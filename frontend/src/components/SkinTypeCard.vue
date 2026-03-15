<script setup>

import { ref } from 'vue'

const selected = ref(null)

const types=[

"Very Fair",

"Fair",

"Light",

"Medium",

"Tan"

]

</script>

<template>

<div class="page">

<h1>Find Your Skin Type</h1>

<p>Select the tone closest to your skin</p>

<div

v-for="type in types"

:key="type"

class="card"

@click="selected=type"

>

{{type}}

</div>

<p v-if="selected">

Recommended protection: Always use SPF30+

</p>

</div>

</template>

<style scoped>

.page{

padding:30px;

text-align:center;

}

.card{

background:#eee;

padding:20px;

margin:10px;

border-radius:10px;

cursor:pointer;

}

</style>
