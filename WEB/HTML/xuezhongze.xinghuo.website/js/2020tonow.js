// 2020距离今年的时间
// 获取当前年份
const currentYear = new Date().getFullYear();
// 计算年份差值
const yearDifference = currentYear - 2020;
// 获取显示年份差值的元素
const yearDifferenceElement = document.getElementById('year-difference');
// 更新年份差值的文本内容
yearDifferenceElement.textContent = yearDifference;