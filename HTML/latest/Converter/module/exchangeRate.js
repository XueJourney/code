module.exports = { getExchangeRate };


let fetch;
import('node-fetch').then(module => {
    fetch = module.default;
});

function getExchangeRate(from, to) {
    const apiKey = process.env.API_KEY;
    const apiUrl = `https://v6.exchangerate-api.com/v6/${apiKey}/latest/${from}`;

    return fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                // 如果响应状态码不是 2xx，抛出错误
                throw new Error(`API request failed with status ${response.status}`);
            }
            return response.text(); // 先获取文本内容
        })
        .then(text => {
            try {
                const data = JSON.parse(text); // 尝试解析JSON
                return data.rates[to]; // 返回目标货币的汇率
            } catch (error) {
                // 如果解析JSON失败，抛出错误
                throw new Error('Failed to parse response as JSON');
            }
        })
        .catch(error => {
            // 捕获并转发任何错误
            console.error('Error in getExchangeRate:', error.message);
            throw error;
        });
}

module.exports = getExchangeRate;
