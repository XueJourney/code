#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from flask import Flask

def readenv():
    tem =open("./idcard/.env", "r")
    env = json.loads(tem.read())
    tem.close()
    # print(env)
    global appCode
    appCode = env['appCode']
    global url
    url = env['url']
    # print(appCode,url)

def requesting(idcard,name):
    data={
        "idcard":idcard,
        "name":name
    }
    headers = {'Authorization':'APPCODE ' + appCode}
    try:
        # 主方法:调用requests
        import requests
        req = requests.post(url,headers=headers,data=data)
        res = req.json()
    except:
        # 报错则使用urllib
        try:
            import urllib3
            http = urllib3.PoolManager()
            encoded_data = json.dumps(data).encode('utf-8')
            response = http.request(
                'POST',  # 或者 'GET', 根据你的需要
                url,
                body=encoded_data,
                headers=headers
            )
            content = response.data
            if content:
                res = content.decode('utf-8')
        except urllib3.exceptions.HTTPError as e:
            # 处理 HTTP 错误
            res = str(e)
    # print(res)
    return res