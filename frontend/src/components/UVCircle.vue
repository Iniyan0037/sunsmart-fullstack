<script setup>

import { computed } from "vue"

const props = defineProps({

uv:Number,
risk:String

})

const color = computed(()=>{

if(props.uv<=2) return "#4CAF50"

if(props.uv<=5) return "#FFEB3B"

if(props.uv<=7) return "#FF9800"

if(props.uv<=10) return "#F44336"

return "#9C27B0"

})

</script>

<template>

<div class="circle" :style="{background:color}">

<h1>{{uv}}</h1>

<p>UV Index</p>

<strong>{{risk}}</strong>

</div>

</template>

<style scoped>

.circle{

width:180px;
height:180px;

border-radius:50%;

display:flex;

flex-direction:column;

align-items:center;
justify-content:center;

margin:30px auto;

font-size:30px;

color:white;

animation:pop 0.6s ease;

}

@keyframes pop{

0%{
transform:scale(0.5);
}

100%{
transform:scale(1);
}

}

</style>
