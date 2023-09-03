import tkinter as tk
from PIL import Image, ImageFont, ImageDraw

# GUI界面
window = tk.Tk()
window.title('明信片生成程序')

# 界面元素
template_img = tk.PhotoImage(file='template.png') 
lbl_template = tk.Label(window, image=template_img)
lbl_template.pack()

text_input = tk.Text(window, height=5)
text_input.pack() 

font_combo = tk.ttk.Combobox(window, values=['Arial', 'Courier', 'Times'])
font_combo.pack()

sv_path = tk.StringVar()
entry_save = tk.Entry(window, textvariable=sv_path)
entry_save.pack()

btn_generate = tk.Button(window, text='生成明信片', command=generate_postcard)
btn_generate.pack()

# Postcard类
class Postcard:

  def __init__(self, template, text, font):
    self.template = template
    self.text = text
    self.font = font

  # 加载字体
  def load_font(self, font):
    fnt = ImageFont.truetype(font, 36)
    return fnt

  # 生成明信片
  def generate(self, save_path):
    img = Image.open(self.template)
    draw = ImageDraw.Draw(img)
    text_to_add = wrap_text(self.text) # 处理自动换行

    # 添加文本
    draw.text((10, 10), text_to_add, font=self.font, fill='#555')

    # 添加景观图片 
    landscape_img = Image.open('landscape.png') 
    landscape_img.thumbnail((300, 200))
    img.paste(landscape_img, (100, 300))

    # 保存图片
    img.save(f'{save_path}/postcard.jpg')

# 生成事件处理
def generate_postcard():
  text = text_input.get('1.0', tk.END)
  font = load_font(font_combo.get())  
  save_path = sv_path.get() 

  postcard = Postcard(template_img, text, font)
  postcard.generate(save_path)

if __name__ == '__main__':
  window.mainloop()