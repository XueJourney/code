// 获取时间并更新页面上的元素
function updateCurrentTime() {
    const currentTimeElement = document.getElementById("current-time");
    if (currentTimeElement) {
        const now = new Date();
        const formattedTime = now.toLocaleTimeString(); // 格式化为本地时间字符串
        currentTimeElement.textContent = formattedTime;
    }
}

// 每秒更新一次时间
setInterval(updateCurrentTime, 1000);