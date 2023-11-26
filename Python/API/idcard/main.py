#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.parse
import urllib
import urllib.request
import json

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

def requesting():
    data={
        "idcard":"身份证号",
        "name":"姓名"
    }
    headers = {'Authorization':'APPCODE ' + appCode}
    fdata = urllib.parse.urlencode(data).encode(encoding='UTF8')
    req = urllib.request.Request(url,headers=headers,data=fdata)
    try:
        response = urllib.request.urlopen(req)
        content = response.read()
        if content:
            print(content.decode('UTF-8'))
    except urllib.error.HTTPError as e:
            print(e.read().decode('UTF-8'))