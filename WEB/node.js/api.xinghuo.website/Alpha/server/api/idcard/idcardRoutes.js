const { handleRequest } = require('./routing');

function setupIdcardRoutes(app, idcardRateLimiter) {
    // 配置POST请求路由
    app.post('/api/idcard', idcardRateLimiter, (req, res) => {
        handleRequest(req, res, 'POST');
    });
    // 配置GET请求路由
    app.get('/api/idcard', idcardRateLimiter, (req, res) => {
        handleRequest(req, res, 'GET');
    });
}

module.exports = setupIdcardRoutes;