#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python review_capture.py  'url' 'text_name'

# 必要なライブラリのインポート
import requests
import lxml.html
from xml.etree.ElementTree import *
import pandas as pd
from pandas import DataFrame as df
from bs4 import BeautifulSoup
import sys


def review_capture(url,text_name):    
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'lxml')
    customers = soup.find_all('a', class_='rvw-item__title-target')
    reveiw_url = list()
    for customer in customers:
        c=customer.get("href")
        reveiw_url.append(c)    
        
    url_df= 'https://tabelog.com' + pd.Series(reveiw_url)
    all_text = url_df.apply(lambda x : requests.get(x))
    all_content = all_text.map(lambda x : x.content)
    all_soup = all_content.map(lambda x : BeautifulSoup(x, 'lxml'))
    all_review = all_soup.apply(lambda x : x.find_all('div', class_="rvw-item__rvw-comment" ))
    
    start_num  = all_review.apply(lambda x : str(x).find('<p>') )
    end_num = all_review.apply(lambda x : str(x).find('</p>') )
    part_review = all_review.apply(lambda x : str(x)[start_num[len(x)]+5: end_num[len(x)]-9])
    
    review_contents =[]
    for i in range(len(part_review)):
            dic =str.maketrans("", "", "<br/>\n</p></div>[]")
            nakami = part_review[i].translate(dic) 
            #ta =part_review[i].replace('<br/>', ' ')
            if i==0:
                f = open(text_name, 'w')  #書き込みモードでオープン
                f.write(nakami)
            else:
                f = open(text_name, 'a')  #追加書き込みモードでオープン
                f.writelines(nakami)
    return 

if __name__ == '__main__':
    url= sys.argv[1]
    text_name= sys.argv[2]
    review_capture(url,text_name)