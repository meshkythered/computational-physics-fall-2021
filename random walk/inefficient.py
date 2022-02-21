# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:54:33 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
import random
import numpy as np
import statistics
import math
import pandas as pd
import time
start_time = time.time()


p=.5

fin_t=[]
POS= np.arange(-10,11)
for pos in range (-10,11):
    T=[]
    N=100000
    for n in range (0,N):
        x=pos
        t=0
        while x<11 and x>-11:
            if np.random.random()<p:
                x+=1
            else:
                x-=1
            t+=1
        T.append(t)
        
    fin_t.append(np.average(T))
    
    
rand_start_avgt=np.average(fin_t)
'''
avglifetime = pd.DataFrame({'start pos':POS, 'avg lifetime':fin_t}) #for the data
datatoexcel = pd.ExcelWriter('avg lifetime inefficient -_-.xlsx')

avglifetime.to_excel(datatoexcel)

datatoexcel.save()'''
print("--- %s seconds ---" % (time.time() - start_time)) #runtime