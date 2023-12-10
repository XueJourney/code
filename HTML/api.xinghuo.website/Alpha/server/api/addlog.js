const fs = require('fs');
const winston = require('winston');
require('winston-daily-rotate-file');

// 确保总目录存在
const logDirectory = './logs/general';
fs.existsSync(logDirectory) || fs.mkdirSync(logDirectory);

// 创建一个新的带有每日轮替文件传输功能的 Winston 日志记录器实例
const dailyRotateFileTransport = new winston.transports.DailyRotateFile({
    filename: `${logDirectory}/%DATE%.log`,
    datePattern: 'YYYY-MM-DD'
});

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        dailyRotateFileTransport
    ]
});

function setuplogRoutes(app) {
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