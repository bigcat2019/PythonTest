# coding:utf-8
import urllib
import Command
import sys
from bs4 import BeautifulSoup
import re
import os

def Main(url):
    print "正在执行任务".decode('UTF-8').encode('GBK') 
    htmlCode=Command.getHtmlCodeByUrl(url,"UTF-8")
    soup = BeautifulSoup(htmlCode, 'html.parser', from_encoding='UTF-8')
    # 查找 class= me1 clearfix 的ul 标签
    lis = soup.find("ul",attrs={"class":"me1 clearfix"}).find_all("li")     
    filepath="D:\Pythons\爬虫\data.json".decode('UTF-8').encode('GBK') 
    fileObject = open(filepath,"w") 
    x=0
    for li in lis:
        tagA= li.find("a")
        tagSpan= li.find("span",attrs={"class":"tip"})
        tagH3= li.find("h3")
        alt= tagA["title"].strip() 
        name= tagH3.find("a").string.strip()
        url= "https://www.80s.tw/"+tagA["href"].strip()
        image= "https:"+tagA.find("img",attrs={"class":"p"})["src"].strip()
        desr= tagSpan.string.strip()
        dataJson="{\"alt\":\""+alt+"\", \"name\":\""+name+"\", \"url\":\""+url+"\", \"image\":\""+image+"\", \"desc\":\""+desr+"\"}"
        if x == 0 :
          fileObject.write("[") 
        if x > 0 :
          fileObject.write(",") 
        fileObject.write(dataJson)  
        x += 1
    fileObject.write("]") 
    fileObject.close()  

#开始执行项目
url="https://www.80s.tw/movie/list"
#设置当前默认编码
reload(sys)  
sys.setdefaultencoding('utf8')   
Main(url) 