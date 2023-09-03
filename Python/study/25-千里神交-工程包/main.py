# 导入模块
from PIL import Image,ImageDraw,ImageFont
import numpy as np

# 定义main函数,函数有三个参数,分别表示背景图片，邮票图片，风景图片的文件名
def main(bg_img,ticket_img,scene_img):
    # 分别读取三个图像的数据并转换为RGBA色彩类型
    bg_img = Image.open(bg_img).convert('RGBA')
    ticket_img = Image.open(ticket_img).convert('RGBA')
    scene_img = Image.open(scene_img).convert('RGBA')
    # 将Image对象转为numpy数组类型
    pic = np.array(bg_img)
    # ticket_img = np.array(ticket_img)
    # scene_img = np.array(scene_img)
    # 将列表[0,0,0,70]转换为数组temp并设置为元组元素类型为uint8
    temp = np.array([0,0,0,70],dtype=np.uint8)
    # 将自定义数组和图片数组相减
    pic = pic - temp
    # 将numpy数组转为Image对象bg
    bg = Image.fromarray(pic)
    # 加载字体文件,并创建字体对象f1并设置字体大小
    f1 = ImageFont.truetype('FangZhengKaiTiJianTi-1.ttf',20)
    # 在背景图片上创建ImageDraw对象d
    d = ImageDraw.Draw(bg)
    # 使用循环在(100,50)坐标处连续绘制6个矩形,每个矩形间隔为25,长度都为20,填充(fill)为白色，边框(outline)为红色,边框(width)宽为2
    for i in range(6):
        d.rectangle((100+i*25,50,100+(i+1)*25,70),fill='white',outline='red',width=2)
    # 使用循环在(400,250)坐标处连续绘制3条横线,横线上下间隔为50,长度为200，颜色设置为silver
    for i in range(3):
        d.line((400,250+i*50,600,250+i*50),fill='silver')
    # 在(40,300)处绘制文字"落霞与孤鹜齐飞,秋水共长天一色",字体颜色设置为黑色,字体设置为f1
    d.text((40,300),'落霞与孤鹜齐飞,秋水共长天一色',fill='black',font=f1)
    # 将风景图片缩小4倍和邮箱图片缩小8倍
    scene_img.thumbnail((scene_img.size[0]//4,scene_img.size[1]//4))
    ticket_img.thumbnail((ticket_img.size[0]//8,ticket_img.size[1]//8))
    # 将邮票图片和风景图片分别粘贴到背景的(550,20)和(50,110)处
    bg.paste(ticket_img,(550,20))
    bg.paste(scene_img,(50,110))
    # 将背景图片保存为"card.png"
    bg.save('card.png')

# 调用main函数
if __name__ == '__main__':
    main('bg.jpg','p.jpg','v.jpg')
    print('图片生戏后,跟目录下card.png')
    print('欢迎下次使用')
    print('代码仅仅为了满足note使用,完其它功胯后台将不再替代')