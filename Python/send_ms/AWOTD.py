# 星火一眼
import json
# 用户信息类
class User():
    def __init__(self):
        # 访问用户信息文件
        # 获取相对路径下的./info/user_info.json
        user_info = open('./info/user_info.json', 'w+', encoding='utf-8')
        # 读取文件(str格式)
        user_info_json = user_info.read()
        # 判断文件内容是否为空
        if user_info_json == {}:
            user_info_json = {
                "user":{
                    "用户ID":{
                        "user_name": "示例数据",
                        "password": "123456",
                        "phone": "13800138000",
                        "email": "example@example.com",
                        "qq": "123456789",
                        "wechat": "wechat",
                        "weibo": "weibo",
                        "address": "address",
                        "introduce": "introduce",
                        "admin": False
                    },
                    "任务":{
                        "星火一言_mail":[],
                        "星火一言_sms":[]
                    }
                }
            }
            user_info.write(user_info_json)
        # 读取文件(json格式)
        self.user_info_json = json.load(user_info)
        # 关闭文件
        user_info.close()
        # 返回json格式数据
    def _debug(self):
        # 输入所有变量
        print(self.user_info_json)
if __name__ == "__main__":
    user = User()
    user._debug()