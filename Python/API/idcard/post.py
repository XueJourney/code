import requests

def authenticate(idcard, name):
    url = "https://api.xinghuo.website/api/idcard"
    params = {
        "idcard": idcard,
        "name": name
    }
    response = requests.get(url, params=params)
    response2 = requests.post(url, data=params)
    # result = response.json()
    return [(response, response2),(response.json(), response2.json())]

idcard = "123456789101"
name = "张三"
result = authenticate(idcard, name)
print(result)