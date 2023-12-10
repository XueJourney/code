const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
  mode: 'development', // 或 'production'
  entry: './src/main.js', // 应用程序的入口点
  output: {
    path: __dirname + '/dist', // 输出目录
    filename: 'bundle.js' // 输出文件名
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin()
  ],
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  }
};
