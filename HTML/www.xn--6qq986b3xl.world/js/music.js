// 创建按钮点击事件处理函数
function handleLoadMusicClick() {
    // 创建一个数组，包含多个音乐播放器的网址
    const musicPlayerUrls = [
        "https://music.163.com/outchain/player?type=2&id=2066608949&auto=1&height=32",//下个路口见
        "https://music.163.com/outchain/player?type=2&id=2031184412&auto=1&height=32",//我曾爱过一个人
        "https://music.163.com/outchain/player?type=2&id=1297802566&auto=1&height=32",//十年人间
        // 添加更多音乐播放器的网址
    ];

    // 从数组中随机选择一个网址
    const randomIndex = Math.floor(Math.random() * musicPlayerUrls.length);
    const selectedUrl = musicPlayerUrls[randomIndex];

    const iframe = document.createElement('iframe');
    iframe.frameBorder = "no";
    iframe.border = "0";
    iframe.marginwidth = "0";
    iframe.marginheight = "0";
    iframe.width = 298;
    iframe.height = 52;
    iframe.src = selectedUrl; // 将随机选择的网址赋给iframe的src属性

    const nav = document.querySelector('nav'); // 选择一个合适的位置插入
    nav.appendChild(iframe);

    // 隐藏按钮
    document.getElementById('loadMusicButton').style.display = 'none';
}