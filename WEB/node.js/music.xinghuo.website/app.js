// 前端
const express = require('express');
const app = express();
app.use(express.json());
const rateLimit = require('express-rate-limit');
const cors = require('cors');
const path = require('path');
// 后端请求库
const axios = require('axios');
const fs = require('fs');
const winston = require("winston");

// Winston logger
const logger = winston.createLogger({
        level: 'info',
        format: winston.format.json(),
        defaultMeta: { service: 'my-service' },
        transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
        new winston.transports.File({ filename: 'combined.log' })
    ]
});

// 静态文件服务
// app.use(express.static('public'));

// 速率限制
const limiter = rateLimit({
    windowMs: 60 * 1000, // 1 minute
    max: 60 // 60 requests per windowMs
});
app.use(limiter);

// CORS 配置
const corsOptions = {
    origin: ['https://static.xinghuo.website',"http://154.12.26.52:7008/"], // 允许的来源
    methods: 'GET', // 允许的 HTTP 方法
    allowedHeaders: ['Content-Type'], // 允许的头部
    optionsSuccessStatus: 200 // 旧浏览器支持的成功状态码
};
// 应用 CORS 中间件
app.use(cors(corsOptions));

// 定义字典ID
var id_ = {};
// 随机ID
function generateId(info) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let id = ''; // 使用let而不是const
    for (let i = 0; i < 10; i++) {
        id += characters.charAt(Math.floor(Math.random() * characters.length));
    }

    // 判断ID是否重复
    if (id in id_) {
        return generateId(); // 如果重复，则递归调用生成新的ID
    }
    // 添加id
    id_[id] = info;
    return id;
}

// 路由
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname,'/public/index.html'));
});
app.get('/home', (req, res) => {
    res.sendFile(path.join(__dirname,'/public/home.html'));
});
app.get('/music', (req, res) => {
    res.sendFile(path.join(__dirname,'/public/music.html'));
});

app.post('/api/music_info', async (req, res) => {
    // 获取参数music_name,singer,key
    const {music_name,singer,key} = req.body;
    // console.log(music_name,singer,key); // 打印请求体中的参数信息
    logger.info(music_name,singer,key);
    // 获取key.json的信息
    const key_info = require('./key.json');
    // 判断key是否存在
    if(key_info[key]){
        // key_info[key]的值减一
        key_info[key] -= 1;
        // 写入key.json
        fs.writeFileSync('./key.json', JSON.stringify(key_info));
        // 生成id
        const id = generateId([{key:[key,key_info[key]]},music_name,singer]);
        // console.log(id);
        logger.info(id);
        // 返回id
        res.json({"ms":"success","id":id});
        // 进行请求
        const response = await axios.get(`http://music.api.xinghuo.website/search?keywords=${music_name}`)
        // response添加至id_[id]的列表后面
        id_[id].push(response.data);
    }else{
        res.json({"ms":"error_key","id":generateId("error_key")});
        logger.error({"ms":"error_key","id":generateId("error_key")});
    }
});
app.get('/api/id',async (req, res) => {
    // 获取参数id
    const {id} = req.query;
    // console.log(id); // 打印请求体中的参数信息
    logger.info(id);
    if(!id_[id]){
        res.json(id_);
    }else{
        res.json(id_[id]);
    }
});

// 设置变量PORT
const PORT = process.env.PORT || 7010;
app.listen(PORT, () => {
    console.log('Server listening on port '+PORT);
});