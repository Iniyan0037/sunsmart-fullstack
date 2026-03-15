<script setup>

import HeaderNav from '../components/HeaderNav.vue'

</script>

<template>

<HeaderNav/>

<div class="page">

<h1>Sun Protection Advice</h1>

<p>

Different UV levels require different protection strategies.
Understanding how to protect your skin can help reduce the risk of sunburn and skin cancer.

</p>

<h2>Protection Guidelines</h2>

<table>

<tr>
<th>UV Index</th>
<th>Risk Level</th>
<th>Recommended Protection</th>
</tr>

<tr>
<td>0 – 2</td>
<td>Low</td>
<td>Sunglasses recommended.</td>
</tr>

<tr>
<td>3 – 5</td>
<td>Moderate</td>
<td>Use sunscreen SPF30+ and wear sunglasses.</td>
</tr>

<tr>
<td>6 – 7</td>
<td>High</td>
<td>Wear sunscreen SPF30+, a hat and sunglasses.</td>
</tr>

<tr>
<td>8 – 10</td>
<td>Very High</td>
<td>Seek shade and reduce sun exposure.</td>
</tr>

<tr>
<td>11+</td>
<td>Extreme</td>
<td>Avoid the sun and stay indoors if possible.</td>
</tr>

</table>

</div>

</template>

<style scoped>

.page{
padding:40px;
text-align:center;
}

table{
margin:auto;
margin-top:20px;
border-collapse:collapse;
}

th, td{
border:1px solid #ccc;
padding:10px 20px;
}

th{
background:#f5f5f5;
}

</style>