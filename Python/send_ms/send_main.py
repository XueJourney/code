# 星火团队短信发送服务
print("服务正在启动,请稍后...")
print("导入库")
import urllib
import urllib.request
import hashlib
import requests
# 导入邮件模块
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
print("正在配置短信宝API")

"""短信宝API"""
# coding=utf-8

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

statusStr = {
    '0': '短信发送成功',
    '-1': '参数不全',
    '-2': '服务器空间不支持,请确认支持curl或者fsocket,联系您的空间商解决或者更换空间',
    '30': '密码错误',
    '40': '账号不存在',
    '41': '余额不足',
    '42': '账户已过期',
    '43': 'IP地址限制',
    '50': '内容含有敏感词'
}

smsapi = "http://api.smsbao.com/"
print("短信宝API配置完成")

# 短信类
class SMS():
    def __init__(self):
        self.user = 'Mr_Xue'
        self.password = 'ec65ec719082e7bd172f81f907e85cf4'
    def send_ms(self,phone,content):
        # 要发送的短信内容
        # content = '短信内容'
        # 要发送短信的手机号码
        # phone = '*****'
        data = urllib.parse.urlencode({'u': self.user, 'p': self.password, 'm': phone, 'c': content})
        send_url = smsapi + 'sms?' + data
        print(send_url)
        response = urllib.request.urlopen(send_url)
        print(response.read().decode('utf-8'))
        the_page = response.read().decode('utf-8')
        # print(statusStr[the_page])
        # return statusStr[the_page]
        print(statusStr)

class mail():
    def __init__(self):
        # 从./info/mail.json获取
        """
        内容格式
        {
            "SMTP": {
                "get":{
                "收件服务器": "imap.exmail.qq.com",
                "使用SSL": true,
                "端口号": 993
                },
                "send":{
                "发件服务器": "smtp.exmail.qq.com",
                "使用SSL": true,
                "端口号": 465
                }
            },
            "星火产品":{
                "邮箱地址": "product@xinghuo.website",
                "密码": "Rh2uQpunBGH6T9yC"
            },
            "server":{
                "邮箱地址": "server@xinghuo.website",
                "密码": "4tAEfdsTazsux2KC"
            },
            "星火广告":{
                "邮箱地址": "ads@xinghuo.website",
                "密码": "6iK8SZJJDrU84rdJ"
            }
        }
        """
        # 读取文件(json格式)
        # mail_info = open('./info/mail.json', 'r', encoding='utf-8')
        # self.mail_info_json = json.load(mail_info)
        self.mail_info_json = requests.get("https://static.xinghuo.website/item_info/info/mail.json").json()
        # 设置邮件信息
        self.send_from = self.mail_info_json['SMTP']['send']['发件服务器']
        self.send_from_port = self.mail_info_json['SMTP']['send']['端口号']
        self.send_from_ssl = self.mail_info_json['SMTP']['send']['使用SSL']
    def send_mail(self, mail_to,  content, Subject,user_name, send_user):
        """
        发送一封电子邮件。
        参数:
        mail_to (str)：收件人的电子邮件地址。
        content (str)：邮件的内容。
        Subject (str)：邮件的主题。
        user_name (str): 获取邮件人的名称。
        send_user (str)：发送邮件的账户。
        """
        # 发件人邮箱地址
        from_email = self.mail_info_json[send_user]['邮箱地址']
        print(from_email)
        # 发件人密码
        password = self.mail_info_json[send_user]['密码']
        # 创建邮件
        msg = MIMEMultipart()
        send_ms = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>%s</title><style>@font-face {font-family: 'SquareRegularScript';src: url('https://static.xinghuo.website/ttf/Square_regular_script.ttf') format('truetype');}body {font-family: Arial, sans-serif;background-color: #f5f5f5;margin: 0;padding: 0;color: #333333;}.email-container {max-width: 600px;margin: 0 auto;background-color: #ffffff;border-radius: 10px;box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);overflow: hidden;}.header {text-align: center;padding: 30px 0;background-color: #f9f9f9;}.header img {width: 100%%;max-width: 200px;height: auto;}.content {padding: 20px 30px;font-size: 14px;font-family: 'SquareRegularScript', Arial, sans-serif;position: relative;min-height: 0px;}.content h2 {font-size: 20px;margin-bottom: 15px;color: #333333;}.content p {font-size: 16px;margin-bottom: 10px;line-height: 1.6;}.signature {text-align: center;padding: 15px 0;font-size: 14px;font-family: 'SquareRegularScript', Arial, sans-serif;color: #666666;}.menu {text-align: center;min-height: 50px;}.menu a {color: #007bff;text-decoration: none;margin: 0 10px;/*@media (prefers-color-scheme: dark) {body {background-color: #1a1a1a;color: #f0f0f0;}.email-container {background-color: #292929;box-shadow: 0 2px 10px rgba(255, 255, 255, 0.1);}.header {background-color: #222222;}.content {background-color: #292929;}.signature {background-color: #222222;}.menu a {color: #4a90e2;}}*/</style></head><body><div class="email-container"><div class="header"><img src="https://static.xinghuo.website/sign/Logo_Colorful_transparent_background.png" alt="星火团队标志"></div><div class="content"><h2>【星火团队】尊敬的%s您好，</h2><p>%s</p></div><div class="signature">祝好，<br>星火团队</div><div class="menu"><a href="https://about.xinghuo.website">关于我们</a></div></div></body></html>""" %(Subject,user_name,content)
        msg.attach(MIMEText(send_ms,'html','utf-8'))
        msg['Subject'] = Header(Subject,'utf-8')
        msg['From'] = Header(from_email,'utf-8')
        print(msg['From'])
        msg['To'] = Header(mail_to,'utf-8')
        # 添加邮件内容
        try:
            # 连接到SMTP服务器
            if self.send_from_ssl:
                server = smtplib.SMTP_SSL(self.send_from, self.send_from_port)
            else:
                server = smtplib.SMTP(self.send_from, self.send_from_port)
            print(server.login(from_email, password))
            # 发送邮件
            print(server.sendmail(from_email, mail_to, msg.as_string()))
            # 关闭连接
            server.quit()
            print("邮件发送成功！")
        except Exception as e:
            print("邮件发送失败：", str(e))

def main():
    mode = input("请选择您本次发送信息的类型(SMS/mail):")
    if mode == "mail":
        # mail信息发送
        print("您选择的是邮件发送")
        print("正在实例化邮件类")
        print("实例化邮件类结束")
        mail_instance.send_mail(mail_to=input("请输入收件人邮箱:"),content=input("请输入邮件正文:"),Subject=input("请输入邮件主题:"),user_name=input("请输入收件人昵称:"),send_user=input("请输入发送邮箱账号(星火产品/server/星火广告):"))
    elif mode == "SMS":
        # SMS信息发送
        print("您选择的是短信发送")
        print("正在实例化短信类")
        print("实例化短信类结束")
        sms.send_ms(input("请输入收信人号码:"), input("请输入短信内容(仅限报备内容):"))
    else:
        print("输入错误，请重新输入!")
    main()

if __name__ == "__main__":
    sms = SMS()
    mail_instance = mail()
    print("项目启动成功！")
    print("欢迎使用星火在线信息发送服务,本项目为星火内部项目,外人请勿使用！")
    password = requests.get("https://static.xinghuo.website/password/national.json").json()
    # print(password)
    if input("请输入您的密码：") == password["内部信息发送"]:
        main()
    else:
        print("密码错误，请重新重新启动后输入！")