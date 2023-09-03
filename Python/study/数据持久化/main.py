import xlwt
import requests

url = "https://api.codemao.cn/api/fanfic/list/all?sort_id=0&fanfic_type_id=0&status=0&page=0&limit10"

# # 新建工作表对象(excel对象)
# wb = xlwt.Workbook()
# # 给表格设置名字
# sheet = wb.add_sheet("TNT")
# # 向第一个单元格写入数据
# sheet.write(0,0,"999999999")
# # 保存至本地
# wb.save("sb.xls")

re = requests.get(url).json()
ms = re["data"]["fanficList"]
# print(ms,"\n",len(ms))
wb = xlwt.Workbook()
sheet = wb.add_sheet("book")
book = [['书名','作者名','小说类型','简介']]
for i in ms:
    book.append([i['title'],i['nickname'],i['fanfic_type_name'],i['introduction']])
wb = xlwt.Workbook(encoding='utf-8')
sheet = wb.add_sheet('book')
for i in range(len(book)):
    for j in range(len(book[0])):
        sheet.write(i,j,book[i][j])
wb.save("book.xlsx")