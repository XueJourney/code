const axios = require('axios');
const logger = require('./logger'); // 假设有一个用于记录日志的模块

let requestCount = {}; // 用于跟踪请求计数的对象

class RequestLimitError extends Error {
    constructor(message) {
        super(message);
        this.name = "RequestLimitError";
    }
}

async function requestIDCard(idcard, name) {
    // 在这里实现请求限制逻辑
    if (requestCount[name] && requestCount[name] >= 10) {
        throw new RequestLimitError(name + ' 达到请求限制');
    }

    // 增加请求计数
    requestCount[name] = (requestCount[name] || 0) + 1;

    // 现有请求身份证的代码
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
    requestIDCard,
    RequestLimitError
};
