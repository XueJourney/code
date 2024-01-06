// 生成随机颜色
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// 反转颜色
function invertColor(hex) {
    var color = (parseInt(hex.slice(1), 16) ^ 0xFFFFFF).toString(16).padStart(6, '0');
    return `#${color}`;
}

// 更新颜色
function updateColors() {
    var newColor = getRandomColor(); // 新的随机颜色
    var invertedColor = invertColor(newColor); // 新颜色的反色

    document.body.style.transition = 'background-color 1s'; // 平滑背景颜色过渡
    document.body.style.backgroundColor = invertedColor; // 更新背景颜色
    var loader = document.querySelector('.loader');
    loader.style.borderColor = 'transparent'; // 其他边框透明
    loader.style.borderTopColor = newColor; // 更新顶部边框颜色
}

// 确保DOM内容加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    updateColors(); // 初始颜色设置

    setInterval(updateColors, 1000); // 每秒变换颜色

    // 设置随机重定向延迟时间，介于3到7秒之间
    var randomDelay = Math.random() * (7000 - 3000) + 3000;
    setTimeout(function() {
        window.location.href = 'home'; // 确保路径正确
    }, randomDelay);
});
