import requests
import json

"""
部分API,可直接复制使用:https://www.tianqiapi.com/api/?version=v6&appid=74169348&appsecret=ti3VzXtb&city=
https://www.tianqiapi.com/api/?version=v6&appid=1&appsecret=123456&city=
"""

# 查询城市
city = input("请输入查询城市的名字")
# 将API接口拼接完整
url = 'https://www.tianqiapi.com/api/?version=v6&appid=74169348&appsecret=ti3VzXtb&city='
# 访问天气接口获得完整数据
response = requests.get(url)
# 获得返回的城市天气的json数据
info = response.text
re = json.loads(info)
print(re)