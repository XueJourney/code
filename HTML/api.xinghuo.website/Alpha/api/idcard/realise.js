const fs = require('fs');
const moment = require('moment');
const axios = require('axios');

let appCode, url;

function readenv() {
    let rawData = fs.readFileSync('./.env', 'utf8');
    let env = JSON.parse(rawData);
    appCode = env.appCode;
    url = env.url;
}

readenv();

// 创建日志文件夹（如果尚不存在）
function ensureLogDirectoryExists() {
    const successLogDir = './logs/idcard/success';
    const errorLogDir = './logs/idcard/error';

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
    const logFilePath = `./logs/idcard/${logDir}/${logFileName}`;

    let logEntry = `[${currentTime}] Method: ${logData.method}, Headers: ${JSON.stringify(logData.headers)}, Body: ${JSON.stringify(logData.body)}, ID Card: ${logData.idcard}, Name: ${logData.name}`;

    if (responseData) {
        logEntry += `, Response: ${JSON.stringify(responseData)}\n`;
    } else {
        logEntry += '\n';
    }

    fs.appendFileSync(logFilePath, logEntry);
    console.log(logEntry);
}

async function requesting(idcard, name) {
    // 如果输入的name和idcard符合特定条件，则直接返回预设的结果(示例数据)
    if (decodeURIComponent(name) === "张三" && idcard === "123456789101") {
        console.log("Return sample data");
        return {
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
        };
    }

    const params = {
        idcard: idcard,
        name: name
    };
    const headers = {
        Authorization: 'APPCODE ' + appCode
    };

    try {
        console.log(`Sending POST request with Query Params: ID Card: ${idcard}, Name: ${name}`);
        console.log(`Request Headers: ${JSON.stringify(headers)}`);
        console.log(`Request Query Params: ${JSON.stringify(params)}`);

        const response = await axios.post(`${url}?idcard=${encodeURIComponent(idcard)}&name=${encodeURIComponent(name)}`, {}, { headers: headers });
        console.log(`Received response: ${JSON.stringify(response.data)}`);
        return response.data;
    } catch (error) {
        console.error(`Error occurred: ${error.message}`);

        if (error.response) {
            console.error(`Error status: ${error.response.status}`);
            console.error(`Error data: ${JSON.stringify(error.response.data)}`);

            const errorCode = parseInt(error.response.data.code);
            let errorMessage = '未知错误';

            switch (errorCode) {
                case 0:
                    errorMessage = '成功';
                    break;
                case 400:
                    errorMessage = '参数错误';
                    break;
                case 20010:
                    errorMessage = '身份证号为空或非法';
                    break;
                case 20310:
                    errorMessage = '姓名为空或非法';
                    break;
                case 404:
                    errorMessage = '请求资源不存在';
                    break;
                case 500:
                    errorMessage = '系统内部错误，请联系服务商';
                    break;
                case 501:
                    errorMessage = '第三方服务异常';
                    break;
                case 604:
                    errorMessage = '接口停用';
                    break;
                case 1001:
                    errorMessage = '其他错误，以实际返回为准';
                    break;
                default:
                    errorMessage = '维护中';
            }

            throw new Error(errorMessage);
        }

        return error.message;
    }
}

module.exports = {
    writeLog,
    ensureLogDirectoryExists,
    requesting
};