import requests
import tqdm

def authenticate(idcard, name):
    url = "http://127.0.0.1:7005/api/idcard"
    params = {
        "idcard": idcard,
        "name": name
    }
    response = requests.get(url, params=params)
    response2 = requests.post(url, data=params)
    # result = response.json()
    return [(response, response2),(response.text, response2.text)]

idcard = "123456789101"
name = "张三"
result1 = []
result2 = []
for i in tqdm.tqdm(range(50)):
    result1.append(authenticate(idcard, name))
    # result2.append(authenticate(idcard, name))
print(result1)