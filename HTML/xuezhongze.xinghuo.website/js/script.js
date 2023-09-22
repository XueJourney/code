// JavaScript代码用于监听页面滚动事件，根据内容高度决定是否取消固定版权栏
window.addEventListener("scroll", function() {
    var footer = document.getElementById("footer");
    if (footer) {
        var contentHeight = document.body.clientHeight;
        var windowHeight = window.innerHeight;
        if (contentHeight > windowHeight) {
            footer.classList.remove("scroll"); // 取消固定
        } else {
            footer.classList.add("scroll"); // 固定
        }
    }
});
