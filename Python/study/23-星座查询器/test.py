# 导入tkinter模块
import tkinter as tk
from tkinter import ttk

# 导入请求模块
import requests
from bs4 import BeautifulSoup

import time

# 创建窗口
window = tk.Tk()
window.title('星座查询助手')

# 月份下拉菜单
month = tk.StringVar()
month_chooser = ttk.Combobox(window, textvariable=month)
month_chooser['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)  

# 日期下拉菜单
day = tk.StringVar()
day_chooser = ttk.Combobox(window, textvariable=day)  
day_chooser['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                         26, 27, 28, 29, 30, 31)
                         
# 查询函数
def query():
  m = month_chooser.get()
  d = day_chooser.get()
  
  results = get_data(m, d)
  
  result_text.insert(1.0, str(results)+"\n")


# 查询按钮                         
query_btn = ttk.Button(window, text='查询', command=query)

# 结果文本框
result_text = tk.Text(window)

# 计算位置的函数  
def place_components():
  width = window.winfo_width()
  height = window.winfo_height()
  
  # 确定位置
  x = width/15
  y = height/15
  
  # 布局
  month_chooser.place(x=x, y=y-15)
  day_chooser.place(x=x*3, y=y-15)
  query_btn.place(x=x*6, y=y-15)
  result_text.place(x=x, y=y*2, relwidth=0.8, relheight=0.5)
  
# 初始化调用 
place_components()

# 网络请求函数
def get_data(month, day):
    url = 'https://www.d1xz.net/astro/xingzuochaxun/{}-{}.aspx'
    response = requests.get(url.format(month, day))
    html = response.content
    bs = BeautifulSoup(html, 'html.parser')
    list1 = []
    div = bs.find('div', {'class': 'xz_hd_left'})
    list1.append('星座：'+div.a.string)
    table = bs.find('table', {'class': 'mt10'})
    td = table.find_all('td')
    for i, j in zip(td[::2], td[1::2]):
        list1.append(i.string+':'+j.string)
    return list1
  
# 窗口resize处理
def resize(event):
  place_components()
  
window.bind('<Configure>', resize)

# 主事件循环
window.mainloop()