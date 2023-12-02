function rateLimit(options) {
    const { maxRequests, timeWindow } = options;
    const requests = new Map();

    return (req, res, next) => {
        const forwardedIpsStr = req.header('x-forwarded-for');
        const ip = forwardedIpsStr ? forwardedIpsStr.split(',')[0] : req.ip;
        const currentTime = Date.now();

        if (!requests.has(ip)) {
            requests.set(ip, { count: 1, startTime: currentTime });
            return next();
        }

        const data = requests.get(ip);
        if (currentTime - data.startTime <= timeWindow) {
            if (data.count >= maxRequests) {
                return res.status(429).json({ error: 'Too many requests' });
            }
            data.count++;
        } else {
            data.count = 1;
            data.startTime = currentTime;
        }

        return next();
    };
}

module.exports = rateLimit;
