# -*- coding: utf-8 -*-
"""
Created on Tue May 16 00:49:27 2017

@author: Administrator
"""
##This is a helper class for data preparation
class inputData:
    def __init__(self):
        self.keyword = "cpu"
        self.pagenum = 0
        self.url = ""
    def welcome(self):
        print "Welcome to use this demo!"
        print "Warning: The system is not in login mode."
        print "Please contact author immediately for any copyright issue."
    def requestData(self):
        self.keyword = raw_input("please input your keyword")
        while True:
            self.pagenum = raw_input("please input your start page number")
            try:
                int(self.pagenum)
                break
            except ValueError:
                print "Please input an Integer!"
        self.url = "https://www.amazon.com/s/page="+self.pagenum+"&keywords="+self.keyword
    def represent(self):
        print "the keyword is:"+self.keyword
        print "the pagenum is:"+self.pagenum
        print "the url is:"+self.url
        
            