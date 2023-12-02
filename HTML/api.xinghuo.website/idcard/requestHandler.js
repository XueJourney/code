// 导入必要的模块
const fs = require('fs').promises; // Using promises for asynchronous file operations
const axios = require('axios');
const config = require('../config');

// 读取和写入请求次数的函数 (改为异步版本)
const readRequestCounts = async () => {
    try {
        const data = await fs.readFile('./idcard/logs/requestCounts.json', 'utf8');
        return JSON.parse(data);
    } catch (err) {
        // 如果文件不存在，返回一个空对象
        return {};
    }
};

const writeRequestCounts = async (counts) => {
    await fs.writeFile('requestCounts.json', JSON.stringify(counts, null, 2));
};

// 带有查询限制的修改后的requesting函数
const requesting = async (idcard, name) => {
    if (!idcard || !name) {
        // console.error('ID card or name is missing or invalid.');
        return;
    }

    // 读取当前的请求次数
    let requestCounts = await readRequestCounts();

    // 获取今天的日期作为字符串
    const today = new Date().toISOString().split('T')[0];

    // 检查该姓名是否有条目以及日期是否为今天
    if (requestCounts[name] && requestCounts[name].date === today) {
        // 检查请求限制是否达到
        if (requestCounts[name].count >= config.dailyRequestLimit) {
            // console.log(`已达到${name}的请求限制`);
            return;
        }
        requestCounts[name].count += 1; // 增加计数
    } else {
        // 重置或初始化这个名字的计数
        requestCounts[name] = { count: 1, date: today };
    }

    // 将更新后的计数写入文件
    await writeRequestCounts(requestCounts);

    // 现有的发起请求的代码
    // console.log('Requesting...');
    const params = {
        idcard: idcard,
        name: name
    };
    const headers = {
        Authorization: 'APPCODE ' + config.idcard_appCode
    };

    try {
        const response = await axios.post(`${config.idcard_url}?idcard=${encodeURIComponent(idcard)}&name=${encodeURIComponent(name)}`, {}, { headers: headers });
        // console.log(`Received response: ${JSON.stringify(response.data)}`);
        return response.data;
    } catch (error) {
        // console.error(`Error occurred: ${error.message}`);

        if (error.response) {
            // console.error(`Error status: ${error.response.status}`);
            // console.error(`Error data: ${JSON.stringify(error.response.data)}`);

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
                    errorMessage = '未知错误';
            }
            throw new Error(errorMessage);
        }

        return error.message;
    }
};

module.exports = requesting;
