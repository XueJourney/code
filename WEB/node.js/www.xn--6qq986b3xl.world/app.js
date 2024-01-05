const express = require('express');
const fs = require('fs');
const helmet = require('helmet');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit'); // 添加缺失的导入

const app = express();
const port = 7001;

app.use(express.static('public'));

const web_page = {};

function readPage(directory, fileName) {
    return new Promise((resolve, reject) => {
        const filePath = `${directory}/${fileName}`;
        let fileContent = '';

        const readStream = fs.createReadStream(filePath, { encoding: 'utf8' });

        readStream.on('data', (chunk) => {
            fileContent += chunk;
        });

        readStream.on('end', () => {
            web_page[fileName] = fileContent;
            resolve();
        });

        readStream.on('error', (err) => {
            console.error('读取文件出错:', err);
            reject(err);
        });
    });
}

const limiter = rateLimit({
    windowMs: 60 * 1000, // 1 minute
    max: 60,
    keyGenerator: (req) => req.ip,
    handler: (req, res) => {
        res.status(429).send(web_page["error_429.html"]); // 使用正确的文件名
    },
});

Promise.all([
    readPage('./error/', '404.html'),
    readPage('./error/', '429.html'),
    readPage('./HTML/', 'index.html'),
    readPage('./HTML/', 'ownership.html'),
    // readPage('./error/', 'error_500.html')
])
.then(() => {
    app.use(helmet());
    app.use(morgan('combined'));
    // app.use(morgan('dev'))

    // CSP配置
    app.use(
        helmet.contentSecurityPolicy({
            directives: {
                defaultSrc: ["'self'"], // 默认只允许从当前域名加载内容
                scriptSrc: ["'self'", "https://static.xinghuo.website","https://cdn.bootcdn.net"], // 允许从当前域名和 static.xinghuo.website 加载脚本
                styleSrc: ["'self'", "https://static.xinghuo.website","https://cdn.jsdelivr.net"], // 允许从当前域名和 static.xinghuo.website 加载样式
                imgSrc: ["'self'", "https://static.xinghuo.website"], // 允许从当前域名和 static.xinghuo.website 加载图片
                fontSrc: ["'self'", "https://static.xinghuo.website"], // 允许从当前域名和 static.xinghuo.website 加载字体
                connectSrc: ["'self'", "https://v.api.aa1.cn"],
            },
        })
    );

    app.use((req, res, next) => {
        res.set('Content-Type', 'text/html; charset=utf-8');
        next();
    });

    const routes = express.Router();
    routes.get(['/', '/index', '/index.html'], (req, res) => {
        res.send(web_page["index.html"]);
    });
    routes.get(['/ownership', '/ownership.html'], (req, res) => {
        res.send(web_page["ownership.html"]); // 修复文件名
    });
    app.use(routes);

    app.use(limiter);

    // 404 错误处理
    app.use((req, res, next) => {
        if (!res.headersSent) {
            res.status(404).send(web_page["error_404.html"]);
        }
    });

    // 500 错误处理
    // app.use((err, req, res, next) => {
    //     console.error(err.stack);
    //     res.status(500).send(web_page["error_500.html"]);
    // });

    app.listen(port, () => {
        console.log(`服务器启动成功，服务运行在端口：${port}`);
    });
})
.catch(err => {
    console.error('加载页面文件时出错:', err);
});
