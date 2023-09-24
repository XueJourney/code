// 文字逐渐显示
// 获取包含文本的容器
const textContainer = document.getElementById('text-container');
const textLines = textContainer.querySelectorAll('p');
const animationDuration = 1000; // 1秒
const delayBetweenLines = 1000; // 1秒
const waitDuration = 3000; // 3秒（等待时间）
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

    // 如果该行是等待行，则添加额外的等待时间
    if (line.classList.contains('wait')) {
        delay += waitDuration;
    }

    line.style.animationDelay = `${delay}ms`;
    delay += animationDuration + delayBetweenLines;
});


// 2020距离今年的时间
// 获取当前年份
const currentYear = new Date().getFullYear();

// 计算年份差值
const yearDifference = currentYear - 2020;

// 获取显示年份差值的元素
const yearDifferenceElement = document.getElementById('year-difference');

// 更新年份差值的文本内容
yearDifferenceElement.textContent = yearDifference;