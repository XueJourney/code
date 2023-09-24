'''图片加工工厂'''
#this
# 导入tkinter库
from tkinter import *
from PIL import Image
from random import randint, choice
#请在下方函数中输入代码
def fil_pic_w():
    '''素描滤镜窗口'''

#请在下方函数中输入代码
def fil_pic():
    '''素描滤镜函数'''

if __name__ == '__main__':
    # 创建主窗口
    w = Tk()
    # 设置主窗口的名字和大小
    w.title('图片处理工厂')
    w.geometry('600x400')
    # 设置主窗口的背景
    c = Canvas(w, width=600, height=400, bg='dimgray')
    c.pack()
    # 创建三个功能按钮
    b1 = Button(
        w, # 对应窗口
        width=12, # 外边框宽度
        height=5, # 外边框长度
        text=" 图片裁剪 ", # 按钮文本
        relief=FLAT, # 按钮样式
        bg='deepskyblue', # 按钮背景颜色
        fg='white', # 文本颜色
        font=('微软雅黑', 15), # 文本字体和大小
        # command=cut_pic_w # 按下时运行的函数
        )
    b1.pack()
    c.create_window(300, 200, window=b1)
    b2 = Button(
        w,
        width=12,
        height=5,
        text=" 素描滤镜 ",
        relief=FLAT,
        bg='tomato',
        fg='white',
        font=('微软雅黑', 15),
        command=fil_pic_w # 按下时运行的函数
        )
    b2.pack()
    c.create_window(120, 200, window=b2)
    b3 = Button(
        w,
        width=12,
        height=5,
        text=" 验证生成 ",
        relief=FLAT,
        bg='gold',
        fg='white',
        font=('微软雅黑', 15),
        # command=code_maker_w 按下时运行的函数
        )
    b3.pack()
    c.create_window(480, 200, window=b3)
    # 增加一些装饰性的文字描述
    c.create_text(300, 60, text='图片处理工厂', fill='white', font=('微软雅黑', 15))
    c.create_text(115, 300, text='· 素描滤镜', fill='white', font=('微软雅黑', 9))
    c.create_text(295, 300, text='· 图片裁剪', fill='white', font=('微软雅黑', 9))
    c.create_text(480, 300, text='· 随机字母', fill='white', font=('微软雅黑', 9))
    # 开启窗口主循环
    w.mainloop()
