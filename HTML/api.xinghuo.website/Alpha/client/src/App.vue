<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  // 这里可以添加必要的逻辑
};
</script>

<style>
:root {
    --background-color-light: #f0f2f5;  /* 亮色主题背景色 */
    --text-color-light: #000000;        /* 亮色主题文字色 */
    --background-color-dark: rgba(0, 0, 0, 0.637);   /* 暗色主题背景色 */
    --text-color-dark: #f0f2f5;         /* 暗色主题文字色 */
    /* 其他需要的变量 */
}

@media (prefers-color-scheme: dark) {
    :root {
        --background-color: var(--background-color-dark);
        --text-color: var(--text-color-dark);
    }
}
@media (prefers-color-scheme: light) {
    :root {
        --background-color: var(--background-color-light);
        --text-color: var(--text-color-light);
    }
}

</style>