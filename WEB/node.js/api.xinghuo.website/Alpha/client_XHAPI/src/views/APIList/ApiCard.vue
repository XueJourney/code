<template>
  <div class="api-card">
    <div class="api-header">
      <span class="api-tag" v-if="tag">{{ tag }}</span>
      <span class="api-author">{{ author }}</span>
    </div>
    <img :src="imageUrl" :alt="name" class="api-icon" />
    <h3>{{ name }}</h3>
    <p>{{ description }}</p>
    <button class="button button-primary" @click="jump">详情</button>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    description: String,
    imageUrl: String,
    tag: String,
    author: String, // 新增
    url: String
  },
  methods: {
    jump() {
      // 跳转到详情页
      this.$router.push(this.url)
    }
  }
}
</script>

<style scoped>
.api-card {
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 200px;
  padding: 15px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.api-icon {
  width: 50px; /* 根据实际情况调整 */
  height: auto;
  margin-bottom: 10px;
}

.api-card h3 {
  color: #333333;
  font-size: 16px;
  margin-top: 10px;
}

.api-card p {
  color: #666666;
  font-size: 14px;
  margin-bottom: 10px;
}

.api-tag {
  background-color: #007bff;
  color: white;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
  margin-bottom: 10px;
}

.button {
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
  color: white;
  background-color: #007bff;
}

.button-primary:hover {
  background-color: #0056b3;
}

.api-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.api-author {
  background-color: #28a745; /* 可根据需要更改颜色 */
  color: white;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
  margin-bottom: 10px;
}
</style>
