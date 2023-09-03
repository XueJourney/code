// 获取每日一言内容
fetch('https://v.api.aa1.cn/api/yiyan/index.php')
    .then(response => response.text())
    .then(data => {
        const quoteElement = document.getElementById('daily-quote');
        quoteElement.textContent = '每日一言：' + stripHtmlTags(data);
    })
    .catch(error => {
        console.error('获取每日一言失败：', error);
    });

// 辅助函数：去除HTML标签
function stripHtmlTags(html) {
    let tmp = document.createElement('DIV');
    tmp.innerHTML = html;
    return tmp.textContent || tmp.innerText || '';
}