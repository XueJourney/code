const express = require('express');
const app = express();
const port = 7001;

app.use(express.static('public'));

const fs = require('fs');

function readPage(filePath, variableName) {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error('读取文件出错:', err);
            return;
        }
            // 将文件内容赋值给指定变量名
            global[variableName] = data;
        });
    }

// 调用函数读取页面文件
readPage('./error/404.html', 'error_404');
readPage('./HTML/index.html', 'index');
readPage('./HTML/ownership.html', 'ownership');


app.get(['/', '/index'], (req, res) => {
   // 设置title标签为域名正在出售! - 我爱你.world
    res.set('Content-Type', 'text/html; charset=utf-8');
    res.send(index);
});

app.get('/ownership', (req, res) => {
    // 设置title标签为域名正在出售! - 我爱你.world
    res.set('Content-Type', 'text/html; charset=utf-8');
    res.send(ownership);
});

// 设置404页面
app.use((req, res, next) => {
    res.status(404).send(error_404);
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});