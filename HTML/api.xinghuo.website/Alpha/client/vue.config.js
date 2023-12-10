const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    port: 7006,
    host: 'doc.api.xinghuo.website'
  },
  publicPath: './',
  transpileDependencies: true
})