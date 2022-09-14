# break和continue的使用
# while True:
#     print("who are you")
#     name = input()
#     if name != "joe":
#         continue
#     while True:
#         print('Hello, Joe. What is the password? (It is a fish.)')
#         password = input()
#         if password == 'swordfish':
#             break
#     break
#
# print("Access granted")

# print函数sep=','为打印多个元素时用什么元素隔开。默认是空格，end="."是print打印的结尾以什么元素结束。默认是换行结束
# print('cats', 'dogs', 'mice', sep=',', end=".")

# 棋盘
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
# printBoard(theBoard)


# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# import re
#
#
# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search("The adventure of Batman and Batwoman")
# print(mo.group())




# 装饰器
# import pytest
#
# data_1 = [
#     {
#         'user': 1,
#         'pwd': 2
#     },
#     {
#         'user': 3,
#         'pwd': 4
#     }
# ]
#
#
# @pytest.mark.parametrize('dic', data_1)
# def test_parametrize_1(dic):
#     print(f'测试数据为\n{dic}')


# fixture用法

# import pytest
#
#
# @pytest.fixture(scope="class")
# def test_01():
#     a = 6
#     b = 7
#     return (a, b)
#
#
# @pytest.fixture(scope="class")
# def test_02():
#     print("你是第二个执行")
#
#
# @pytest.mark.usefixtures("test_02")
# @pytest.mark.usefixtures("test_01")  # 优先执行
# class TestNum:
#     def test_03(self, test_01):
#         a = test_01[0]
#         b = test_01[1]
#         assert a < b
#         print("断言成功")



# bs4 爬虫
# from bs4 import BeautifulSoup
# r = requests.get(url, data=None, headers=header)  # 获取requests请求对象的返回值
# r = r.content() # 将返回值转化为二进制形式
# soup = BeautifulSoup(r, 'lxml')  # 利用BeautifulSoup()将二进制形式的r通过lxml HTML解析器解析
# print(soup.title)  # 获取返回值网页数据中<title>xxxx</title>的数据
# print(soup.title.string)  # 获取返回值网页数据中<title>xxx</title>标签之间的值，也可用soup.title.text
# print(soup.title.name)  # 获取<title>xxx</title>标签的名字title
# print(soup.a['href'])  # 匹配第一个<a>xxx</a> a标签之间的值中href的取值
# print(soup.find_all("input")[2]["value"])  # find_all()方法找到所有input的匹配值，
# # 再通过编号[2]取第三个，然后["value"]取value的值
# print(soup.title.children) # 获取title标签的子标签
# print(soup.title.parent) # 获取title标签的父标签
# print(soup.findall(attrs={"id":"link1"}))  # 匹配attrs(参数)为id=link1的标签
# print(soup.findall(class_="sister"))  # 匹配class=sister的标签
#
#
# html = '''
# <html><head><title>The Dormouse's story</title></head>
#     <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# '''



# 设置发送请求的代理ip
# import requests
#
# proxy = {
#     'http': '59.48.200.158:9091'
# }
#
# response = requests.get("http://httpbin.org/ip",proxies=proxy)
# print(response.text)


# webdriver简单应用

# from selenium import webdriver  # 导入模块
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()  # 创建一个浏览器实例
# driver.get("http://www.baidu.com") # 使用get方法访问指定url
# driver.maximize_window() # 最大化浏览器
# driver.find_element(By.ID, 'kw').clear()  # 对定位element进行清除内容操作
# driver.find_element(By.ID, 'kw').send_keys('淘宝网')  # 对定位element进行输入操作
# driver.find_element(By.ID, 'su').click()  # 对定位element进行鼠标左键点击操作
# time.sleep(5)
# driver.quit() # 退出浏览器
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://wenku.baidu.com/view/95dd5cc1bb4cf7ec4afed0f1.html?fr=income1-doc-search'
# header = {'User-agent': 'Googlebot'}
# res = requests.get(url, headers=header)
# soup = BeautifulSoup(res.text, "html.parser")
# plist = []
# print(soup)
# for div in soup.find_all('div', attrs={"class": "bd doc-reader"}):
#     plist.extend(div.get_text().split('\n'))
# print(plist)

# yield的用法
# def both(N):
#     for i in range(N):
#         yield i
#     yield 3
#     for i in (x**2 for x in range(N)):
#         yield i
#
#
# print(list(both(5)))

import os
import requests
import pytest
from utils.requestutils import request_send
from testcases.yamlfiles.getYamlPath import readYamlCase
from utils.readYamlCase import run_yaml


@pytest.mark.parametrize('caseInfo', readYamlCase("test01.yaml"))
def test_01(caseInfo):
    run_yaml(caseInfo)











