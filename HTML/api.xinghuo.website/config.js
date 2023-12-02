const fs = require('fs');

function readenv() {
    let rawData = fs.readFileSync('./.env', 'utf8');
    let env = JSON.parse(rawData);
    console.log(env);
    console.log({
        idcard_appCode: env.idcard.appCode,
        idcard_url: env.idcard.url
    });
    return {
        idcard_appCode: env.idcard.appCode,
        idcard_url: env.idcard.url
    };
}

module.exports = readenv();
