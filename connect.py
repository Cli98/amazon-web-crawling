# -*- coding: utf-8 -*-
"""
Created on Tue May 16 01:10:52 2017

@author: Administrator
"""
import requests
from lxml import etree
##This is a class to connect to amazon
class connect:
    def __init__(self,url):
        self.head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
        }
        self.url = url
    def conn(self):
        html = requests.get(self.url, headers=self.head)
        selector = etree.HTML(html.text)
        content = selector.xpath("//html")
        return content
    def getHeader(self,content):
        title = content[0].xpath("//head//title/text()")
        return title
        
        