const express = require('express');
const bodyParser = require('body-parser');
// idcard模块
const requesting = require('./idcard/requestHandler');
const { ensureLogDirectoryExists, writeLog } = require('./idcard/logger');
// 访问量限制
const rateLimit = require('./rateLimit'); // 引入新的限流模块

const app = express();
app.use(bodyParser.json());

app.use(rateLimit({ maxRequests: 10, timeWindow: 1000 })); // 应用限流中间件

// 处理POST请求
app.post('/api/idcard', async (req, res) => {
    try {
        const { idcard, name } = req.query;
        const result = await requesting(idcard, name);

        // 记录成功的请求，包括响应数据
        writeLog(true, {
            method: 'POST',
            headers: req.headers,
            body: req.body,
            idcard,
            name
        }, result);

        res.json(result);
    } catch (error) {
        // 记录失败的请求，包括错误信息
        writeLog(false, {
            method: 'POST',
            headers: req.headers,
            body: req.body,
            idcard: req.query.idcard,
            name: req.query.name
        }, { error: error.message });

        res.status(500).json({ error: error.message });
    }
});

// 处理GET请求
app.get('/api/idcard', async (req, res) => {
    try {
        const { idcard, name } = req.query;
        const result = await requesting(idcard, name);

        // 记录成功的请求，包括响应数据
        writeLog(true, {
            method: 'GET',
            headers: req.headers,
            body: req.body,
            idcard,
            name
        }, result);

        res.json(result);
    } catch (error) {
        // 记录失败的请求，包括错误信息
        writeLog(false, {
            method: 'GET',
            headers: req.headers,
            body: req.body,
            idcard: req.query.idcard,
            name: req.query.name
        }, { error: error.message });

        res.status(500).json({ error: error.message });
    }
});

const PORT = 7005;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

ensureLogDirectoryExists();
