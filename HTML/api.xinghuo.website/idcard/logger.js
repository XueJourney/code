const fs = require('fs');
const moment = require('moment');

function ensureLogDirectoryExists() {
    const successLogDir = './idcard/logs/success';
    const errorLogDir = './idcard/logs/error';

    if (!fs.existsSync(successLogDir)) {
        fs.mkdirSync(successLogDir, { recursive: true });
    }

    if (!fs.existsSync(errorLogDir)) {
        fs.mkdirSync(errorLogDir, { recursive: true });
    }
}

function writeLog(isSuccess, logData, responseData = null) {
    const currentDate = moment().format('YYYY-MM-DD');
    const currentTime = moment().format('YYYY-MM-DD HH:mm:ss.SSS');
    const logFileName = `${currentDate}.log`;
    const logDir = isSuccess ? 'success' : 'error';
    const logFilePath = `./logs/${logDir}/${logFileName}`;

    let logEntry = `[${currentTime}] Method: ${logData.method}, Headers: ${JSON.stringify(logData.headers)}, Body: ${JSON.stringify(logData.body)}, ID Card: ${logData.idcard}, Name: ${logData.name}`;

    if (responseData) {
        logEntry += `, Response: ${JSON.stringify(responseData)}\n`;
    } else {
        logEntry += '\n';
    }

    fs.appendFileSync(logFilePath, logEntry);
    console.log(logEntry);
}

module.exports = {
    ensureLogDirectoryExists,
    writeLog
};
