#导入爬虫库和数据处理库
import requests
from bs4 import BeautifulSoup
# 导入time
import time


# 拼接网站链接并请求该网址
def get(month,day):
    url= "https://www.d1xz.net/astro/xingzuochaxun/{}-{}.aspx"
    response = requests.get(url.format(month,day))
    # 获取完整源码
    html = response.content
    # 使用bs进行解析
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    list_1 = []
    # 获取class为xz_hs_left的所有标签(提取星座名字)
    # print(soup)
    div = soup.find('div', {'class':'xz_hd_left'})
    # print(div)
    list_1.append("星座:"+div.a.string)
    # 获取class为mt10的所有标签(获取星座详细信息)
    table = soup.find('div', class_='mt10')
    td = table.find_all('td')
    # 输出调试信息(全部变量信息)
    # print(td,"/n",table)
    # 遍历td列表
    # 使用time获取程序运行时间
    t_1 = time.perf_counter()
    # for i,j in zip(td[::2],td[1::2]):
    #     # print(i.string,j.string)
    #     list_1.append(i.string+":"+j.string)
    # 使用time获取程序运行时间
    # Use zip and a generator expression to append elements to list_1
    list_1.extend(i.string + ":" + j.string for i, j in zip(td[::2], td[1::2]))
    t_2 = time.perf_counter()
    print("循环运行时间:",t_2-t_1,"秒")
    return list_1

# 测试
if __name__ == "__main__":
    # 调用get
    print(get("8","22"))