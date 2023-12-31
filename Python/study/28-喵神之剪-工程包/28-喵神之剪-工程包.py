'''图片加工工厂'''

# 导入库
from tkinter import *
from PIL import Image

#请在下方函数中输入代码
def cut_pic_w():
    '''图片裁剪窗口'''
    w1 = Tk()
    w1.title('图片裁剪')
    w1.geometry('400x200')
    # 创建画布c1
    c1 = Canvas(w1, width=400, height=200, bg='deepskyblue')
    # 指定布局方式
    c1.pack()
    # 文件名name，左上角坐标(x1,y1)，右下角坐标(x2,y2)
    global name, x1, y1, x2, y2
    name = Text(w1, width=30, height=1)
    name.pack()
    # 将文本组件放置到画布上
    c1.create_window(200, 60, window=name)
    # 坐标
    x1 = Text(w1, width=7, height=1)
    x1.pack()
    c1.create_window(120, 100, window=x1)
    y1 = Text(w1, width=7, height=1)
    y1.pack()
    c1.create_window(220, 100, window=y1)
    x2 = Text(w1, width=7, height=1)
    x2.pack()
    c1.create_window(120, 130, window=x2)
    y2 = Text(w1, width=7, height=1)
    y2.pack()
    c1.create_window(220, 130, window=y2)
    # 创建按钮
    b = Button(w1, text='确定', command=cut_pic)
    b.pack()
    # 将按钮放置到画布上
    c1.create_window(320, 170, window=b)
    # 显示窗口
    w1.mainloop()


#请在下方函数中输入代码
def cut_pic():
    '''图片裁剪函数'''
    # 获取图片名字
    # print(name.get(1.0, END))
    n = str(name.get(1.0, END)).strip()
    # 获取坐标
    x_start = int(x1.get(1.0, END))
    y_start = int(y1.get(1.0, END))
    x_end = int(x2.get(1.0, END))
    y_end = int(y2.get(1.0, END))
    # 打开图片
    img = Image.open(n)
    # 裁剪图片
    img = img.crop((x_start, y_start, x_end, y_end))
    # 保存图片
    name = n.split("/")
    img.save(name[0:len(name)-1]+'cut_' + name[len(name)-1])
    print('图片裁剪成功')



#图片处理工厂主界面
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
        command=cut_pic_w # 按下时运行的函数
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
        # command=fil_pic_w # 按下时运行的函数
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
        # command=code_maker_w
        )
    b3.pack()
    c.create_window(480, 200, window=b3)
    # 增加一些装饰性的文字描述
    c.create_text(300, 60, text='图片处理工厂', fill='white', font=('微软雅黑', 15))
    c.create_text(115, 300, text='· 素描滤镜', fill='white', font=('微软雅黑', 9))
    c.create_text(295, 300, text='· 图片裁剪', fill='white', font=('微软雅黑', 9))
    c.create_text(480, 300, text='· 随机字母', fill='white', font=('微软雅黑', 9))
    # 刷新主窗口
    w.mainloop()
