import requests
import re
import xlrd as xl
import pytest
from bs4 import BeautifulSoup
# import socket
# socket.setdefaulttimeout(15)


def check_title(url, title, description1):
    header = {
        "Connection": "close",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    r = requests.get(url, headers=header)

    if r.status_code != 200:
        print(f"Error code: {r.status_code}")
    res = r.text
    html = BeautifulSoup(res, 'html.parser')
    title1 = html.title.string   # 获取title里面的内容
    description = html.find(attrs={"name": "description"})['content']
    if description.strip() != description1.strip():
        print(f"Error description:\n{description1}\n{description} ")
    if title1 != title:
        print(f"Error title: {title}")


def get_data_from_excel():
    xls_file = xl.open_workbook("./test.xlsx")#打开文件
    # print(len(xls_file.sheets()))#获得表格工作簿的个数（包括空的工作簿）
    xls_sheet = xls_file.sheets()[0]#打开文件簿，第一个文件簿用[0]表示

    # print(xls_sheet.nrows)#返回工作簿的行数
    # print(xls_sheet.ncols)#返回工作簿的列数

    li = []
    for i in range(132):
        row_value = xls_sheet.row_values(i)#第一行所有的值
        li.append(row_value)

    print(len(li))

    for j in range(80, 133):
        url = li[j][0].replace("www.malts", "malts:Classic@123@secure-malts.diageoplatform")
        title = li[j][2]
        description = li[j][3]
        check_title(url, title, description)
        print(f"{j} success")


get_data_from_excel()
