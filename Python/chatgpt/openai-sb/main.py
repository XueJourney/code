import requests
import json

# 定义获取配置文件
def get_config(web):
    if web == "openai-sb":
        info_file = "./info.json"
        with open(info_file, "r", encoding="utf-8") as info_tem:
            info = json.load(info_tem)
        print("测试信息", "配置文件", info)
        return info
    else:
        return None

# 进行请求-chatgpt
def request_chatgpt(key, web, version, problem):
    # 设置post请求体
    messages = [{"role": "system", "content": "你是星火团队旗下的一个AI助手，你的工作是帮助用户解答疑问"}, {"role": "user", "content": problem}]
    data = {
        "model": version,
        "prompt": problem,
        # "max_tokens": 7,  # 将字符串 '7' 改为整数 7
        # "temperature": 0.7,  # 设置一个介于0和1之间的浮点数
        # "top_p": 1,
        # "n": 1,
        # "stream": "false"
    }
    # 设置请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + key
    }
    # 设置代理
    proxies = None  # 如果不需要代理，设置为None

    # 进行请求
    print("测试信息", "请求信息", web, headers, data, proxies)
    response = requests.post(web, headers=headers, data=data, proxies=proxies)

    if __name__ == "__main__":
        # 输出响应的JSON数据
        print(response.json())

if __name__ == "__main__":
    config = get_config("openai-sb")
    request_chatgpt(config["key"], "https://api.openai-sb.com/v1/chat/completions", "gpt-3.5-turbo-0613", "Say this is a test")