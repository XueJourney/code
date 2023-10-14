const express = require('express');
const fs = require('fs');
const rateLimit = require("express-rate-limit");

const app = express();
const port = 7001;

// 从 'public' 目录提供静态文件
app.use(express.static('public'));

// 定义一个函数，用于从文件中读取页面内容
function readPage(filePath, variableName) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                console.error('读取文件出错:', err);
                reject(err);
            } else {
                global[variableName] = data;
                resolve();
            }
        });
    });
}

// 中间件，用于记录请求信息
function logRequestInfo(req, res, next) {
    const timestamp = new Date().toISOString();
    const userIP = req.socket.remoteAddress;
    const requestMethod = req.method;
    const requestHeaders = JSON.stringify(req.headers, null, 2);

    const logMessage = `${timestamp}\n请求 URL: ${req.url}\n用户 IP: ${userIP}\n请求方法: ${requestMethod}\n请求头信息: ${requestHeaders}\n\n`;

    console.log(logMessage);

    const now = new Date();
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0');
    const day = now.getDate().toString().padStart(2, '0');
    const logFileName = `${year}${month}${day}.log`;

    const logPath = `./log/${logFileName}`;
    fs.appendFile(logPath, logMessage, (err) => {
        if (err) {
            console.error('写入日志文件出错:', err);
        }
    });

    next();
}

readPage('./error/429.html', 'error_429')
const limiter = rateLimit({
    windowMs: 60 * 1000, // 1 minute
    max: 60,
    keyGenerator: (req) => req.ip,
    handler: (req, res) => {
        // Send a 429 response with the custom message
        res.status(429).send(error_429);
    },
});

// 使用 Promise 来确保页面文件加载完成
Promise.all([
    readPage('./error/404.html', 'error_404'),
    readPage('./HTML/index.html', 'index'),
    readPage('./HTML/ownership.html', 'ownership')
])
.then(() => {
    app.use(logRequestInfo);
    app.use(limiter);

    // 设置路由
    app.get(['/', '/index', '/index.html'], (req, res) => {
        res.set('Content-Type', 'text/html; charset=utf-8');
        res.send(index);
    });

    app.get(['/ownership', '/ownership.html'], (req, res) => {
        res.set('Content-Type', 'text/html; charset=utf-8');
        res.send(ownership);
    });

    app.use((req, res, next) => {
        const status = res.statusCode;
        if (status === 404) {
            res.send(error_404);
        } else {
            next();
        }
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