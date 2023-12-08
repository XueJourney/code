const { requesting, writeLog, ensureLogDirectoryExists } = require('./realise');
// 确保日志目录存在
ensureLogDirectoryExists();

// 基于姓名的请求限制设置
const nameRequestCounts = {}; // 用于存储基于姓名的请求计数的对象

// 获取当前日期的函数
// 用于跟踪每天的请求次数
function getCurrentDate() {
    // 将日期格式化为 YYYY-MM-DD
    return new Date().toISOString().split('T')[0];
}

// 更新姓名请求计数的函数
// 如果请求次数超过限制，则返回 false
function updateNameRequestCount(name) {
    const currentDate = getCurrentDate();
    // 如果是首次请求，则初始化计数
    if (!nameRequestCounts[name]) {
        nameRequestCounts[name] = { date: currentDate, count: 1 };
    } else if (nameRequestCounts[name].date === currentDate) {
        // 如果是当天的后续请求
        if (nameRequestCounts[name].count >= 10) {
            // 如果请求次数超过限制
            return false;
        }
        // 否则增加计数
        nameRequestCounts[name].count += 1;
    } else {
        // 如果是新的一天，则重置计数
        nameRequestCounts[name] = { date: currentDate, count: 1 };
    }
    return true;
}

// 处理请求的通用函数
// 适用于POST和GET请求
async function handleRequest(req, res, method) {
    const { idcard, name } = method === 'POST' ? req.body : req.query;

    // 检查请求次数是否超过限制
    if (!updateNameRequestCount(name)) {
        const errorMessage = '此姓名今日请求限制已达到';
        // 记录请求限制错误
        writeLog(false, { method, headers: req.headers, body: req.body, idcard, name }, { error: errorMessage });
        return res.status(429).json({ error: errorMessage });
    }
        // 如果输入的name和idcard符合特定条件，则直接返回预设的结果(示例数据)
        if (name === "张三" && idcard === "123456789101") {
            console.log("Return sample data");
            res.json({
                "code": "0",
                "message": "成功",
                "result": {
                    "name": "张三",
                    "idcard": "000000000000000",
                    "res": "1",
                    "description": "一致",
                    "sex": "男",
                    "birthday": "00000000",
                    "address": "示例"
                }
            });
        } else{
        try {
            // 发起请求并获取结果
            const result = await requesting(idcard, name);
            // 记录成功的请求
            writeLog(true, { method, headers: req.headers, body: req.body, idcard, name }, result);
            // 返回结果
            res.json(result);
        } catch (error) {
            // 记录API级别的错误
            writeLog(false, { method, headers: req.headers, body: req.body, idcard, name }, { error: error.message });
            // 返回错误信息
            res.status(500).json({ error: error.message });
        }
    }
}


module.exports = {
    handleRequest
};