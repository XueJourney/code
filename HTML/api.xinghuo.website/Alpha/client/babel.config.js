module.exports = {
  presets: [
    [
      "@vue/cli-plugin-babel/preset",
      {
        useBuiltIns: 'usage', // 根据使用情况自动引入 polyfills
        corejs: 3, // 指定 core-js 的版本
        targets: { // 指定目标浏览器
          esmodules: true, // 现代浏览器
        },
      },
    ],
  ],
};
