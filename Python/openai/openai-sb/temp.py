import requests
import json

# 定义API的URL和你的API密钥
url = "https://api.openai-sb.com/v1/engines/davinci-codex/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_OPENAI_KEY"
}

# 定义请求的数据
data = {
    "prompt": "Translate the following English text to French: '{}'",
    "max_tokens": 60
}

# 发送POST请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 打印响应的结果
print(response.json())
