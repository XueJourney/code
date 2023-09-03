import requests
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Inches
import re

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0"}
get_re = requests.get('https://movie.douban.com/chart',headers=header)
html = get_re.text
html = re.sub("<span.?","",html)
html = html.replace("</span>","")
bs = BeautifulSoup(html,"html.parser")
div_list = bs.find_all("div",{"class":"pl2"})
ms = []
def delete(s):
    s = s.replace("","")
    s.replace("\n","")
    return s
for i in div_list:
    name = delete(i.a.string)
    star = i.p.string
    score = delete(i.div.string)
    ms.append(name+"\n"+star+"\n"+score+"\n")

document = Document()
for i in ms:
    document.add_paragraph(i)
document.save("排行榜.docx")