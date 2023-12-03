const express = require('express');
const fs = require('fs');
const axios = require('axios');
const bodyParser = require('body-parser');
const moment = require('moment');

const app = express();
app.use(bodyParser.json());

let appCode, url;

function readenv() {
    let rawData = fs.readFileSync('./.env', 'utf8');
    let env = JSON.parse(rawData);
    appCode = env.appCode;
    url = env.url;
}

readenv();

async function requesting(idcard, name) {
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

// 创建日志文件夹（如果尚不存在）
function ensureLogDirectoryExists() {
    const successLogDir = './logs/success';
    const errorLogDir = './logs/error';

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

// 处理POST请求
app.post('/api/idcard', async (req, res) => {
    res.status(200).json({error:"zh:系统正在维护 en:The system is being maintained"})
    // try {
    //     const { idcard, name } = req.query;
    //     const result = await requesting(idcard, name);

    //     // 记录成功的请求，包括响应数据
    //     writeLog(true, {
    //         method: 'POST',
    //         headers: req.headers,
    //         body: req.body,
    //         idcard,
    //         name
    //     }, result);

    //     res.json(result);
    // } catch (error) {
    //     // 记录失败的请求，包括错误信息
    //     writeLog(false, {
    //         method: 'POST',
    //         headers: req.headers,
    //         body: req.body,
    //         idcard: req.query.idcard,
    //         name: req.query.name
    //     }, { error: error.message });

    //     // 500
    //     res.status(200).json({ error: error.message });
    // }
});

// 处理GET请求
app.get('/api/idcard', async (req, res) => {
    res.status(200).json({error:"zh:系统正在维护 en:The system is being maintained"})
    // try {
    //     const { idcard, name } = req.query;
    //     const result = await requesting(idcard, name);

    //     // 记录成功的请求，包括响应数据
    //     writeLog(true, {
    //         method: 'GET',
    //         headers: req.headers,
    //         body: req.body,
    //         idcard,
    //         name
    //     }, result);

    //     res.json(result);
    // } catch (error) {
    //     // 记录失败的请求，包括错误信息
    //     writeLog(false, {
    //         method: 'GET',
    //         headers: req.headers,
    //         body: req.body,
    //         idcard: req.query.idcard,
    //         name: req.query.name
    //     }, { error: error.message });

    //     // 500
    //     res.status(200).json({ error: error.message });
    // }
});

const PORT = 7005;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

ensureLogDirectoryExists();