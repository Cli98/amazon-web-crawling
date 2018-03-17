# -*- coding: utf-8 -*-
"""
Created on Tue May 16 00:40:26 2017

@author: Administrator
"""

from multiprocessing.dummy import Pool as ThreadPool
import numpy as np
import pandas as pd
from inputData import inputData
from connect import connect
#test on data preparation
inp = inputData()
inp.welcome()
inp.requestData()
inp.represent()

#test on connection
con = connect(inp.url)
content = con.conn()
title = con.getHeader(content)







   