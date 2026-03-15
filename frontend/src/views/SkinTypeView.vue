<template>
  <div class="page">
    <div class="container">
      <h1 class="title">🧑 Skin Type Guide</h1>

      <p class="subtitle">
        Choose the skin tone that best matches your natural skin colour.
      </p>

      <div class="grid">
        <div class="card type1" @click="goType(1)">
          <div class="tone"></div>
          <h3>Very Fair</h3>
          <p>Burns very easily, rarely tans</p>
        </div>

        <div class="card type2" @click="goType(2)">
          <div class="tone"></div>
          <h3>Fair</h3>
          <p>Usually burns, tans slightly</p>
        </div>

        <div class="card type3" @click="goType(3)">
          <div class="tone"></div>
          <h3>Light</h3>
          <p>Sometimes burns, gradually tans</p>
        </div>

        <div class="card type4" @click="goType(4)">
          <div class="tone"></div>
          <h3>Medium</h3>
          <p>Rarely burns, tans easily</p>
        </div>

        <div class="card type5" @click="goType(5)">
          <div class="tone"></div>
          <h3>Tan</h3>
          <p>Very rarely burns, deeply pigmented</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function goType(type) {
  router.push(`/skin/type${type}`);
}
</script>

<style scoped>
/* 1. 确保最外层容器占满整个屏幕，并强制内容居中 */
.page {
  width: 100vw;           /* 使用 vw 确保占据 100% 视口宽度 */
  min-height: 100vh;      /* 使用 vh 确保占据 100% 视口高度 */
  margin: 0;
  padding: 0;             /* 去掉 padding，避免偏移 */

  background: url("../assets/skin.jpg") center center no-repeat;
  background-size: cover;

  display: flex;
  justify-content: center; /* 水平方向居中 */
  align-items: center;     /* 垂直方向居中 */
  
  overflow: hidden;        /* 防止出现滚动条 */
}

/* 2. 内部卡片容器 */
.container {
  width: 90%;             /* 在小屏幕上自适应 */
  max-width: 800px;       /* 最大宽度保持 800px */
  
  background: rgba(0, 0, 0, 0.6);
  padding: 40px;
  border-radius: 20px;
  color: white;
  text-align: center;
  backdrop-filter: blur(8px);
  
  /* 确保没有向左的 margin 偏移 */
  margin: auto;           
}

.title {
  font-size: 36px;
  margin-bottom: 10px;
}

.subtitle {
  opacity: 0.9;
  margin-bottom: 30px;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

/* 移动端适配：如果是手机查看，自动变成一列 */
@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}

.card {
  background: rgba(255, 255, 255, 0.15);
  padding: 25px;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
}

.card:hover {
  transform: translateY(-5px) scale(1.03);
  background: rgba(255, 255, 255, 0.25);
}

.tone {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  margin: 0 auto 15px auto;
  border: 3px solid white;
}

/* Skin Colors */
.type1 .tone { background: #f8e5d8; }
.type2 .tone { background: #f2d3b3; }
.type3 .tone { background: #d9a47a; }
.type4 .tone { background: #b8734e; }
.type5 .tone { background: #8d5524; }

h3 { margin-bottom: 6px; }
p { font-size: 14px; opacity: 0.9; }

</style>