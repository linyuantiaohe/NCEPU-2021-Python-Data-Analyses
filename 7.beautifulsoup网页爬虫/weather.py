#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib.request import urlopen 
from bs4 import BeautifulSoup 
region=[101010100,101130101,101010300,101011200]
for i in region:
    url="http://www.weather.com.cn/weather/"+str(i)+".shtml"
    a=urlopen(url)
    b=BeautifulSoup(a)
    c1=b.find("div",{'class':{"crumbs fl"}})
    regionname=c1.get_text().replace('\n','').replace('>',' ')
    c2=b.find("ul",{'class':{'t clearfix'}}).findAll("li")
    print(c1.get_text().replace('\n','').replace('>',' '),'天气:\n')
    for j in c2:
        print(j.get_text().replace('\n',' '))
    print('-----------------------------')