// 创建按钮点击事件处理函数
function handleLoadMusicClick() {
    // 创建一个数组，包含多个音乐播放器的网址
    const musicPlayerUrls = [
        "https://music.163.com/outchain/player?type=2&id=2066608949&auto=1&height=32", // 下个路口见
        "https://music.163.com/outchain/player?type=2&id=2031184412&auto=1&height=32", // 我曾爱过一个人
        "https://music.163.com/outchain/player?type=2&id=1297802566&auto=1&height=32", // 十年人间
        // 添加更多音乐播放器的网址
    ];

    // 从数组中随机选择一个网址
    const randomIndex = Math.floor(Math.random() * musicPlayerUrls.length);
    const selectedUrl = musicPlayerUrls[randomIndex];

    // 创建一个iframe元素
    const iframe = document.createElement('iframe');
    iframe.setAttribute('frameborder', 'no');
    iframe.setAttribute('border', '0');
    iframe.setAttribute('marginwidth', '0');
    iframe.setAttribute('marginheight', '0');
    iframe.setAttribute('width', '298');
    iframe.setAttribute('height', '52');
    iframe.setAttribute('src', selectedUrl);

    // 找到合适的位置并插入iframe
    const nav = document.querySelector('nav');
    nav.appendChild(iframe);

    // 隐藏按钮
    const loadMusicButton = document.getElementById('loadMusicButton');
    loadMusicButton.style.display = 'none';
}