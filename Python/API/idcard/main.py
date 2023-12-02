import json
import requests

def requesting(idcard, name):
    tem =open("./idcard/.env", "r")
    env = json.loads(tem.read())
    tem.close()
    # print(env)
    global appCode
    appCode = env['appCode']
    global url
    url = env['url']
    # print(appCode,url)
    data = {
        "idcard": idcard,
        "name": name
    }
    headers = {'Authorization': 'APPCODE ' + appCode}
    req = requests.post(url, headers=headers, data=data)
    # print(req.text)
    res = req

    return res

# requesting("440304201008224653","薛中泽")
print(requesting("440304201008224653","薛中泽"))