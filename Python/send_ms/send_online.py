from flask import Flask, render_template, request
import time
import threading
from send_main import SMS, mail

app = Flask(__name__)

# 定义全局的短信和邮件实例
sms_instance = SMS()
mail_instance = mail()

# 存储定时任务的字典
scheduled_tasks = {}

# 定义定时任务函数
def schedule_task(phone, content, mail_to, mail_content, subject, interval):
   while True:
       # 执行短信发送
       sms_instance.send_ms(phone, content)
       
       # 执行邮件发送
       mail_instance.send_mail(mail_to, mail_content, subject, "User", "星火产品")
       
       # 等待指定时间间隔
       time.sleep(interval)

# 定义网页路由
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
   phone = request.form.get('phone')
   content = request.form.get('sms_content')
   mail_to = request.form.get('mail_to')
   mail_content = request.form.get('mail_content')
   subject = request.form.get('subject')
   interval = int(request.form.get('interval'))
   
   # 启动定时任务
   task = threading.Thread(target=schedule_task, args=(phone, content, mail_to, mail_content, subject, interval))
   task.start()
   
   # 将定时任务加入字典
   scheduled_tasks[phone] = task
   
   return "任务已启动"

@app.route('/stop/<phone>')
def stop(phone):
   if phone in scheduled_tasks:
       task = scheduled_tasks[phone]
       task.join()  # 等待任务完成
       del scheduled_tasks[phone]
       return "任务已停止"
   else:
       return "任务不存在"

if __name__ == '__main__':
   app.run(debug=True, port=19007)