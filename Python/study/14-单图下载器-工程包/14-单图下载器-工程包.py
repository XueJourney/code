# 导入库
import requests
# 日志记录
# import logging

# # 配置日志记录
# logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', 
#                     format='%(asctime)s - %(levelname)s - %(message)s')
# # 创建日志记录器
# logger = logging.getLogger('app_log')
# # 创建StreamHandler处理器并设置日志级别
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# # 将处理器添加到日志记录器
# logger.addHandler(stream_handler)


# res_1 = requests.get(url="https://www.httpbin.org/get")
# logger.info(res_1.status_code)
# logger.info(res_1.text)
# res_2 = requests.get("https://www.httpbin.org/get?name=codemao&password=123456")
# logger.info(res_2.status_code)
# logger.info(res_2.text)
# form = {"username":"codemao","password":"123456"}
# res_3 = requests.get("https://www.httpbin.org/get",params=form)
# logger.info(res_3.status_code)
# logger.info(res_3.text)

url = "https://static.codemao.cn/whale/H1X2u2OQO"
res = requests.get(url)
fi = open("test.png","wb")
fi.write(res.content)
fi.close()