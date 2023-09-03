"""文字加密"""
from tkinter import *
import qrcode
from PIL import Image, ImageTk

def generate_qr_code(text,filename):
    qr = qrcode.QRCode(
        version=None,
        box_size=5,
        border=1,
        error_correction=qrcode.ERROR_CORRECT_H
    )
    qr.make(fit=True)
    qr.add_data(text)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save(filename+".png")

def callback():
    text_input = t.get(0.0,"end")
    img_name = text_input[0:1]
    generate_qr_code(text_input,img_name)
    img = Image.open(img_name+".png")
    img = img.resize((300,300))
    img = ImageTk.PhotoImage(img)
    label.configure(image=img)
    label.image = img

root = Tk()
root.title("二维码生成器")

img = qrcode.make("https://www.codemao.cn")
img.save("hello.png")

img = Image.open("hello.png")
img = ImageTk.PhotoImage(img)

t = Text(root,height=10,font=("黑体",15))
t.grid(row=0,column=0,padx=10,pady=5)

btn = Button(root,text="点我生成二维码",width=20,font=("黑体",30),command=callback)
btn.grid(row=1,column=0,pady=20)

label = Label(root,image=img,width=500,height=500)
label.grid(row=2,column=0)

# 创建并运行窗口
root.mainloop()