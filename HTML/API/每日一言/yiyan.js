// 获取每日一言内容
function fetchDailyQuote() {
    const quoteElement = document.getElementById('daily-quote');
    quoteElement.textContent = '每日一言：正在刷新...'; // 显示刷新中的消息

    fetch('https://v.api.aa1.cn/api/yiyan/index.php')
        .then(response => response.text())
        .then(data => {
            quoteElement.textContent = '每日一言：' + stripHtmlTags(data); // 刷新完成后显示内容
        })
        .catch(error => {
            console.error('获取每日一言失败：', error);
        });
}

// 辅助函数：去除HTML标签
function stripHtmlTags(html) {
    let tmp = document.createElement('DIV');
    tmp.innerHTML = html;
    return tmp.textContent || tmp.innerText || '';
}

// 自动刷新每日一言
function autoRefresh() {
    fetchDailyQuote(); // 初始获取一次
    setInterval(() => {
        fetchDailyQuote(); // 每30秒获取一次
    }, 30000); // 30秒
}

// 页面加载完毕后开始自动刷新
window.addEventListener('load', autoRefresh);