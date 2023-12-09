const fs = require('fs');
const winston = require('winston');

// 确保总目录存在
const logDirectory = './logs/general';
fs.existsSync(logDirectory) || fs.mkdirSync(logDirectory);

// 创建一个新的带有文件传输功能的 winston 日志记录器实例
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.File({ filename: `${logDirectory}/${new Date().toISOString().slice(0,10)}.log` })
    ]
});

function setuplogRoutes(app){
    // 记录所有请求的中间件
    app.use((req, res, next) => {
        const logEntry = {
            timestamp: new Date().toISOString(), // ISO string includes milliseconds
            method: req.method,
            path: req.originalUrl,
            body: req.body,
            headers: req.headers
        };
        logger.info(logEntry);
        next();
    });
}

module.exports = {
    logger,
    setuplogRoutes
};