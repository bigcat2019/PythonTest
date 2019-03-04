# coding:utf-8
import urllib
import Command
import sys
from bs4 import BeautifulSoup
import re

def Main():
    print "正在执行任务".decode('UTF-8').encode('GBK') 
    htmlCode=Command.getHtmlCodeByUrl("http://tieba.baidu.com/p/1753935195","UTF-8")
    soup = BeautifulSoup(htmlCode, 'html.parser', from_encoding='UTF-8')
    img_list= soup.find_all('img',attrs={"class":"BDE_Image"})
    x=0
    path="D:\Pythons\爬虫\Images".decode('UTF-8').encode('GBK') 
    print path
    for img in img_list:
        print img['src']
        urllib.urlretrieve(img['src'], path + "/%s.jpg" %x)
        x += 1



#开始执行项目
Main() 
