const express = require('express');
const bodyParser = require('body-parser');
const rateLimit = require('express-rate-limit');
const setupIdcardRoutes = require('./api/idcard/idcardRoutes');
const { logger, setuplogRoutes } = require('./api/addlog');


const app = express();
app.use(bodyParser.json());

// 基于IP的速率限制（每秒20次请求）
const idcardRateLimiter = rateLimit({
    windowMs: 1000, // 1秒
    max: 20, // 每个IP限制每秒20次请求
    message: JSON.stringify({ error: '来自此IP的请求过多，请一秒后再试' })
});

setuplogRoutes(app) // 通用日志记录
setupIdcardRoutes(app, idcardRateLimiter); // idcard API

const PORT = 7005;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});