import requests
import json

# 默认地址需要境外访问
url = 'https://api.gptapi.us/v1/chat/completions'

# 替换为您自己的API密钥
api_key = 'sk-5tqMKtdw71DesKj43e34D1615b2d460cAcA7A3152e19E43d'


def send_message(message):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "gpt-3.5-turbo-1106",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{message}"}
        ]
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    if response.status_code == 200:
        print(response.json())
        print("Message sent successfully!")
        return response.json()["choices"][0]["message"]['content']
    else:
        print(f"Error: {response.status_code}")
        return None


resp = send_message('hello')
print(resp)