from tkinter import *
import time
import random
from PIL import ImageTk

# 创建主窗口
root = Tk()
root.title('英雄之力')
root.geometry('460x300+700+300')

hero_list = [['暗裔剑魔', '1.png', 180, 100, 150, 75],
             ['牛头酋长', '2.png', 180, 200, 100, 120],
             ['冰晶凤凰', '3.png', 270, 120, 180, 175],
             ['潮汐海灵', '4.png', 120, 160, 180, 240],
             ['扭曲树精', '5.png', 200, 160, 140, 290],
             ['迷失之牙', '6.png', 220, 160, 180, 190]]

label1 = Label(root,width=460,height=300)
label1.place(x=0,y=0)

text = StringVar()
label2 = Label(root,font=("Arial,22"),textvariable=text)
label2.place(x=50,y=20)
text.set("请点击按钮")

# label_a设置开始
label_a = Label(root,text="物理攻击:")
label_a.place(x=50,y=80)
# canvas_a设置开始
canvas_a = Canvas(root,width=300,height=22,bg="white")
canvas_a.place(x=110,y=80)
# label_b设置开始
label_b = Label(root,text="魔法攻击:")
label_b.place(x=50,y=120)
# canvas_b设置开始
canvas_b = Canvas(root,width=300,height=22,bg="white")
canvas_b.place(x=110,y=120)
# label_c设置开始
label_c = Label(root,text="防御能力:")
label_c.place(x=50,y=160)
# canvas_c设置开始
canvas_c = Canvas(root,width=300,height=22,bg="white")
canvas_c.place(x=110,y=160)
# label_d设置开始
label_d = Label(root,text="上手难度:")
label_d.place(x=50,y=200)
# canvas_d设置开始
canvas_d = Canvas(root,width=300,height=22,bg="white")
canvas_d.place(x=110,y=200)

def progress():
    canvas_a.delete("all")
    canvas_b.delete("all")
    canvas_c.delete("all")
    canvas_d.delete("all")
    hero_data = hero_list[random.randint(0,len(hero_list)-1)]
    print(hero_data)
    text.set(hero_data[0])
    print("C:\\item\\04-英雄之力-工程包\素材包\\"+hero_data[1])
    img_new = ImageTk.PhotoImage(file="C:\\item\\04-英雄之力-工程包\素材包\\"+hero_data[1])
    label1.configure(image = img_new)
    label1.image = img_new
    n_a = 0
    n_b = 0
    n_c = 0
    n_d = 0
    for i in range(100):
        n_a += hero_data[2]/100
        n_b += hero_data[3]/100
        n_c += hero_data[4]/100
        n_d += hero_data[5]/100
        canvas_a.create_rectangle(0,0,n_a,22,width=0,fill="grey")
        canvas_b.create_rectangle(0,0,n_b,22,width=0,fill="orange")
        canvas_c.create_rectangle(0,0,n_c,22,width=0,fill="blue")
        canvas_d.create_rectangle(0,0,n_d,22,width=0,fill="green")
        root.update()
        time.sleep(0.02)

button = Button(root,text="查看属性",command=progress)
button.place(x=200,y=240)

root.mainloop()
