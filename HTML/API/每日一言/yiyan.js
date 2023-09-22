// 模块化代码

// 获取每日一言内容
async function fetchDailyQuote() {
    try {
        const response = await fetch('https://v.api.aa1.cn/api/yiyan/index.php');
        if (!response.ok) {
            throw new Error('获取每日一言失败');
        }
        const data = await response.text();
        return data;
    } catch (error) {
        throw new Error('获取每日一言失败：' + error.message);
    }
}

// 去除HTML标签
function stripHtmlTags(html) {
    let tmp = document.createElement('DIV');
    tmp.innerHTML = html;
    return tmp.textContent || tmp.innerText || '';
}

// 在页面上显示每日一言
async function displayDailyQuote() {
    const quoteElement = document.getElementById('daily-quote');
    const loadingIndicator = document.getElementById('loading-indicator');

    try {
        loadingIndicator.textContent = '正在刷新...';
        const data = await fetchDailyQuote();
        quoteElement.textContent = '每日一言：' + stripHtmlTags(data);
    } catch (error) {
        console.error(error.message);
        quoteElement.textContent = '获取每日一言失败，请重试。';
    } finally {
        loadingIndicator.textContent = ''; // 清除加载指示器
    }
}

// 自动刷新每日一言
function autoRefreshDailyQuote() {
    setInterval(displayDailyQuote, 30000); // 每30秒刷新一次
}

// 调用函数以初始化自动刷新
displayDailyQuote();
autoRefreshDailyQuote();