# 导入请求库，json库
import requests
import json

# 定义获取配置文件
def get_config(web):
    if web == "openai-sb":
        info_file = "./info.json"
        info_tem = open(info_file, "r", encoding="utf-8")
        info = json.load(info_tem)
        info_tem.close()
        return info
    else:
        return None

