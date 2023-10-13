const express = require('express');
const fs = require('fs');

const app = express();
const port = 7001;

// 设置静态目录
app.use(express.static('public'));

// 调用函数读取页面文件
function readPage(filePath, variableName) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                console.error('读取文件出错:', err);
                reject(err);
            } else {
                // 将文件内容赋值给指定变量名
                global[variableName] = data;
                resolve();
            }
        });
    });
}

// 中间件函数来获取用户IP、请求方式和请求头信息并记录日志
function logRequestInfo(req, res, next) {
    // 获取当前时间戳
    const timestamp = new Date().toISOString();

    console.log('Request URL:', req.url);
    const userIP = req.socket.remoteAddress;
    const requestMethod = req.method;
    const requestHeaders = JSON.stringify(req.headers, null, 2);

    // 格式化日志信息
    const logMessage = `${timestamp}\nRequest URL: ${req.url}\nUser IP: ${userIP}\nRequest Method: ${requestMethod}\nRequest Headers: ${requestHeaders}\n\n`;

    // 输出到控制台
    console.log(logMessage);

    // 保存日志到文件
    const now = new Date();
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0');
    const day = now.getDate().toString().padStart(2, '0');
    const logFileName = `${year}${month}${day}.log`;

    const logPath = './log/' + logFileName;
    fs.appendFile(logPath, logMessage, (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
        }
    });

    next();
}

// 在这里使用 Promise 来确保页面文件加载完成
Promise.all([
    readPage('./error/404.html', 'error_404'),
    readPage('./HTML/index.html', 'index'),
    readPage('./HTML/ownership.html', 'ownership')
])
.then(() => {
    // 使用中间件来获取请求信息
    app.use(logRequestInfo);

    // 设置路由
    app.get(['/', '/index','/index.html'], (req, res) => {
        // 指定响应内容的类型和编码
        res.set('Content-Type', 'text/html; charset=utf-8');
        res.send(index);
    });

    app.get(['/ownership','/ownership.html'], (req, res) => {
        // 指定响应内容的类型和编码
        res.set('Content-Type', 'text/html; charset=utf-8');
        res.send(ownership);
    });

    // 设置404页面
    app.use((req, res, next) => {
        res.status(404).send(error_404);
    });

    // 创建服务器并监听端口
    app.listen(port, () => {
        console.log('服务器启动成功');
        console.log(`服务运行在端口： ${port}`);
    });
})
.catch(err => {
    console.error('加载页面文件时出错:', err);
});