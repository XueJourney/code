const { readenv, requesting } = require('./app');

readenv(); // 确保取消注释此行以设置环境变量

const idcard = '123456789012345678'; // 示例身份证号
const name = '张三'; // 示例姓名

async function testRequesting() {
    try {
        const result = await requesting(idcard, name);
        console.log('Result:', result);
    } catch (error) {
        console.error('Error:', error);
    }
}

testRequesting();
