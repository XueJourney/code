import requests
import tqdm

# def authenticate(idcard, name):
#     url = "http://127.0.0.1:7005/api/idcard"
#     params = {
#         "idcard": idcard,
#         "name": name
#     }
#     response = requests.get(url, params=params)
#     # response2 = requests.post(url, data=params)
#     # result = response.json()
#     return [response,response.text]

# idcard = "123456789101"
# name = "张三"
# # print(authenticate(idcard, name))
result = []
for i in tqdm.tqdm(range(50)):
    result.append(requests.get("https://api.aa1.cn/doc/authenticate.html"))
# result2.append(authenticate(idcard, name))
print(result)