const express = require('express');
const plotly = require('plotly')('MrXue', 'u2EaQYj7xQcib854l1aa'); // 替换为你的Plotly用户名和API密钥
const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.json());

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

// 处理函数绘图请求
app.post('/plot', (req, res) => {
  // 从请求中获取参数
  const { func, minX, maxX, minY, maxY } = req.body;

  // 构建绘图配置
  const trace = {
    x: [], // x轴数据
    y: [], // y轴数据
    type: 'scatter', // 散点图
  };

  // 生成x轴数据
  for (let x = minX; x <= maxX; x += 0.1) {
    trace.x.push(x);
    // 计算对应的y值
    const y = eval(func); // 使用eval执行输入的函数
    trace.y.push(y);
  }

  // 绘制图表
  const figure = { data: [trace] };

  // 使用Plotly生成图像
  plotly.getImage(figure, { format: 'png', width: 800, height: 400 }, (error, imageStream) => {
    if (error) {
      console.error(error);
      res.status(500).send('Error generating plot');
    } else {
      // 将图像数据作为base64发送到前端
      let data = '';
      imageStream.on('data', (chunk) => {
        data += chunk;
      });
      imageStream.on('end', () => {
        const imageBase64 = Buffer.from(data).toString('base64');
        const imageUrl = `data:image/png;base64,${imageBase64}`;
        console.log('Generated image URL:', imageUrl);
        res.send(imageUrl);
      });
    }
  });
});
