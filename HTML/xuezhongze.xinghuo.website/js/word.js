// 文字逐渐显示并带有打字机效果
// 获取包含文本的容器
const textContainer = document.getElementById('text-container');
const textLines = textContainer.querySelectorAll('p');
const animationDuration = 500; // 1秒
const delayBetweenLines = 500; // 1秒
let delay = 0;

textLines.forEach((line) => {
    const styleElement = document.createElement('style');
    styleElement.textContent = `
        @keyframes lineFadeIn {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        .line-fade-in p {
            opacity: 0;
            animation: lineFadeIn ${animationDuration}ms ease-in-out forwards;
        }
    `;

    document.head.appendChild(styleElement);

    // 使用自定义的等待时间参数（传入的值或默认值）
    const waitDuration = parseInt(line.dataset.waitDuration) || 1000;
    delay += waitDuration;

    // 添加打字机效果
    const text = line.textContent;
    line.textContent = ''; // 清空文本
    const textLength = text.length;
    let charIndex = 0;

    function typeText() {
        if (charIndex < textLength) {
            line.textContent += text.charAt(charIndex);
            charIndex++;
            setTimeout(typeText, 100); // 调整打字速度，根据需要修改
        }
    }

    setTimeout(typeText, delay); // 延迟后开始打字

    delay += textLength * 100 + delayBetweenLines;
});

// 为打字效果创建CSS动画
const characterStyleElement = document.createElement('style');
characterStyleElement.textContent = `
    @keyframes characterFadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
`;
document.head.appendChild(characterStyleElement);