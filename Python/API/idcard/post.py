import requests

def authenticate(idcard, name):
    url = "http://api.xinghuo.website/api/idcard"
    params = {
        "idcard": idcard,
        "name": name
    }
    response = requests.get(url, params=params)
    # response2 = requests.post(url, data=params)
    # result = response.json()
    return [response,response.text]

idcard = "123456789101"
name = "张三"
# print(authenticate(idcard, name))
result = []
for i in range(1):
    result.append(authenticate(idcard, name))
# result2.append(authenticate(idcard, name))
print(result)