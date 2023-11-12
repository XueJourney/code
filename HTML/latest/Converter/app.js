const express = require('express');
const morgan = require('morgan');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const fs = require('fs');
// 汇率API
const { getExchangeRate } = require('./module/exchangeRate');

// 配置
const app = express();
require('dotenv').config();
const port = process.env.PORT || 7003;
app.use(express.static('public'));

// 函数读取页面文件
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

// 限制速率
const limiter = rateLimit({
    windowMs: 60 * 1000, // 1 minute
    max: 60,
    keyGenerator: (req) => req.ip,
    handler: (req, res) => {
        res.status(429).send(web_page["error_429.html"]); // 使用正确的文件名
    },
});

// 配置页面路由
Promise.all([
    readPage('./HTML/', 'index.html'),
    readPage('./error/', '404.html')
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
                scriptSrc: ["'self'", "https://static.xinghuo.website"], // 允许从此域名加载脚本
                styleSrc: ["'self'", "https://static.xinghuo.website","cdnjs.cloudflare.com","fonts.googleapis.com"], // 允许从此域名加载样式
                imgSrc: ["'self'", "https://static.xinghuo.website","flagcdn.com"], // 允许从此域名加载图片
                fontSrc: ["'self'", "https://static.xinghuo.website","fonts.gstatic.com","cdnjs.cloudflare.com"], // 允许从此域名加载字体
                connectSrc: ["'self'","https://v6.exchangerate-api.com/v6/c71b33398a0d7d4dacb4a6bd/latest/CNY"], // 允许从此域名引入内容
            },
        })
    );

    app.use((req, res, next) => {
        res.set('Content-Type', 'text/html; charset=utf-8');
        next();
    });

    // 定义页面
    const routes = express.Router();
    app.use((req, res, next) => {
        res.setHeader('X-Content-Type-Options', 'nosniff');
        next();
    });

    routes.get(['/', '/index', '/index.html'], (req, res) => {
        res.send(web_page["index.html"]);
    });

    // API路由
    app.get('/getExchangeRate', (req, res) => {
        const { from, to } = req.query;
        if (!from || !to) {
            return res.status(400).send('Missing required query parameters: from and to');
        }

        getExchangeRate(from, to)
        .then(rates => {
            const exchangeRate = rates[to];
            if (exchangeRate) {
                res.json({ exchangeRate });
            } else {
                res.status(404).send(`Exchange rate not found for ${to}`);
            }
        })
        .catch((error) => {
            console.error('Error fetching exchange rate:', error.message); // 提供更详细的错误信息
            res.status(500).send('Error fetching exchange rate');
        });
    });

    // 路由页面
    app.use(routes);
    // 速率限制
    app.use(limiter);

    // 错误处理
    app.use((req, res, next) => {
        if (!res.headersSent) {
            res.status(404).send(web_page["error_404.html"]);
        }
    });

    app.listen(port, () => {
        console.log(`服务器启动成功，服务运行在端口：${port}`);
    });
})
.catch(err => {
    console.error('加载页面文件时出错:', err);
});
