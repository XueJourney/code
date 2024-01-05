module.exports = { getExchangeRate };

let fetch;
import('node-fetch').then(module => {
    fetch = module.default;
});

function getExchangeRate(from, to) {
    const apiKey = process.env.API_KEY;
    const apiUrl = `https://v6.exchangerate-api.com/v6/${apiKey}/latest/${from}`;

    return fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`API request failed with status ${response.status}`);
            }
            return response.json(); // Directly returning JSON.
        })
        .then(data => data.rates[to])
        .catch(error => {
            console.error('Error in getExchangeRate:', error.message);
            throw error;
        });
}
