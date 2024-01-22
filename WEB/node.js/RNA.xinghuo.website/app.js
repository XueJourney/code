const express = require('express');
const rateLimit = require('express-rate-limit');
const axios = require('axios');
const fs = require('fs');
const path = require('path');


function getLocalIP() {
    const os = require('os');
    const interfaces = os.networkInterfaces();
    for (const name of Object.keys(interfaces)) {
        for (const iface of interfaces[name]) {
            if (iface.family === 'IPv4' && !iface.internal) {
                return iface.address;
            }
        }
    }
}

// 创建 Express 应用
const app = express();

// 定义速率限制规则
const limiter = rateLimit({
    windowMs: 1000, // 1s
    max: 100, // 每个IP 1s内最多100次请求
    message: '请求过于频繁,请在15分钟后重试。Too many requests, please try again after 15 minutes.'
});

app.use(limiter);

// 静态文件服务
app.use(express.static('./public'));


app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/html/index.html');
});
app.get('/home', (req, res) => {
    res.sendFile(__dirname + '/public/html/home.html');
});
app.get('/idcard/', (req, res) => {
    res.sendFile(__dirname + '/public/html/idcard/home.html');
});
app.get('/idcard/accreditation/*', (req, res) => {
    res.sendFile(__dirname + '/public/html/idcard/accreditation.html');
});
app.get('/idcard/result/:id/', async (req, res) =>{
    res.sendFile(__dirname + '/public/html/idcard/result.html');
})

let idData = {}; // 新建一个空字典用于存储每个ID的数据
app.get('/api/idcard/accreditation/:id/:name/:idcard', async (req, res) => {
    const id = req.params.id;
    const name = req.params.name;
    const idcard = req.params.idcard;

    // 创建日志字符串
    let log = `Request received: ID=${id}, Name=${name}, IDCard=${idcard}\n`;

    // 检查id是否为六位数
    if (!/^\d{6}$/.test(id)) {
        // 如果ID不是六位数，返回错误信息
        return res.status(400).json({ error: 'ID必须为六位数' });
    }

    // 检查id是否已经存在于idData字典中
    if (id in idData) {
        // 如果ID已存在，返回重复ID的信息
        return res.status(400).json({ error: '重复ID' });
    }

    if (!/^([1-6][1-9]|50)\d{4}(18|19|20)\d{2}((0[1-9])|10|11|12)(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$/.test(idcard)){
        return res.status(400).json({error:"身份证格式有误"})
    }

    if (!/^[\u4e00-\u9fa5]{2,4}$/.test(name))
    {
        return res.status(400).json({error:"姓名格式有误"})
    }

    try {
        // 使用axios向外部API发送请求
        const response = await axios.post('https://api.xinghuo.website/api/idcard', {
            name: name,
            idcard: idcard
        });

        // 将成功处理的ID及其相关数据保存到字典中
        idData[id] = response.data;
        // 时间
        const now = new Date();
        const formattedDateTime = now.toISOString();
        idData[id].time = formattedDateTime

        // 添加日志
        log += `Success: Data saved for ID=${id}\n`;

        // 发送保存的数据回客户端
        res.json({info:"ok"});
        console.log(idData.id)
    } catch (error) {
        log += `Error: ${error.message}\n`;
        // 处理错误（例如，外部API可能宕机）
        res.status(500).send({error:'Error occurred: ' + error.message});
    } finally {
        // 保存日志到文件
        const now = new Date();
        const logDirectory = './log/' + now.toISOString().split('T')[0];
        if (!fs.existsSync(logDirectory)){
            fs.mkdirSync(logDirectory, { recursive: true });
        }
        const logFile = path.join(logDirectory, `${id}.log`);
        fs.appendFileSync(logFile, log);
    }
});
app.get('/api/idcard/result/:id/', async (req, res) => {
    // 获取ID
    const id = req.params.id;
    console.log("result "+typeof id)

    // 根据ID查询字典idData, 获取result.name、result.idcard、result.description
    const result = idData[id];
    console.log(result)
    console.log(idData)
    if (!result) {
        return res.status(404).json({ message: 'IDNF' });
    }

    // 将身份证(result.idcard)打码，将后4位和前2位替换为*号
    let maskedIdCard = result.result.idcard;
    if (maskedIdCard !== undefined && maskedIdCard !== null && maskedIdCard.length >= 6) {
        maskedIdCard = maskedIdCard.substring(0, 2).replace(/./g, '*') + 
                       maskedIdCard.substring(2, maskedIdCard.length - 4) + 
                       maskedIdCard.substring(maskedIdCard.length - 4).replace(/./g, '*');
    }

    // 返回为json路由
    return res.json({
        message: "ok",
        name: result.result.name,
        idcard: maskedIdCard,
        description: result.result.description,
        time: result.time
    });
});

app.get('/admin/leoxue6464496/idcard/:id/', async (req, res) => {
    const id = req.params.id;
    // 假设idData是一个已定义的字典
    if (id === 'all') {
        // 如果ID等于'all'，返回整个字典
        res.send(idData);
    } else {
        // 如果ID不等于'all'，返回idData[id]的值
        if (idData.hasOwnProperty(id)) {
            // 检查id是否在idData中
            res.send(idData[id]);
        } else {
            // 如果id不在idData中，返回错误信息
            res.status(404).send('ID not found');
        }
    }
});


const PORT = 7009;

// 启动服务器并监听指定端口
app.listen(PORT, async () => {
    console.log(`Server running on port ${PORT}`);

    // 获取并打印内网IP地址
    const localIP = getLocalIP();
    console.log(`内网访问链接: http://${localIP}:${PORT}`);

    try {
        // 异步获取并打印公网IP地址（IPv4和IPv6）
        const publicIpv4 = await publicIp.v4();
        const publicIpv6 = await publicIp.v6();
        console.log(`公网访问链接 IPV4: http://${publicIpv4}:${PORT}`);
        console.log(`公网访问链接 IPV6: [${publicIpv6}]:${PORT}`); // IPv6地址通常需要用方括号括起来
    } catch (error) {
        // console.error('无法获取公网IP地址:', error);
        console.error("无法获取公网IP地址")
    }
});