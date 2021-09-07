# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:14:23 2021

@author: ms2674
"""

import json
import sys


with open(sys.argv[1], encoding="utf-16") as f:
    listDir = json.load(f)
DATA_iter = iter(listDir['DATA'])
len_DATA = len(listDir['DATA'])
size_list=[]
for i in range(len_DATA):
    if listDir['DATA'][i]['type']=='file':
        size_list.append(listDir['DATA'][i]['size'])

print('Total size:',sum(size_list),'Number of files:', len(size_list))

