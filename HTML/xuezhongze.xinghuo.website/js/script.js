// JavaScript代码放在这里
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

    line.style.animationDelay = `${delay}ms`;
    delay += animationDuration + delayBetweenLines;
});