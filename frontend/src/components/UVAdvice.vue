<script setup>

import { computed } from "vue"

const props = defineProps({

uv:Number

})

const message = computed(()=>{

if(!props.uv) return ""

if(props.uv<=2)
return "Low UV risk."

if(props.uv<=5)
return "Moderate UV. Use sunscreen."

if(props.uv<=7)
return "High UV. Wear hat and sunglasses."

return "⚠ Very high UV! Seek shade and avoid midday sun."

})

</script>

<template>

<div v-if="uv" class="advice">

<h3>Protection Advice</h3>

<p>{{message}}</p>

</div>

</template>

<style scoped>

.advice{

margin-top:20px;

background:white;

color:black;

padding:15px;

border-radius:10px;

}

</style>