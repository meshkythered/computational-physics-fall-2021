# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 19:33:24 2021

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

T=1000
finst=np.zeros (T)
N=10000
for k in range (0,5):
    fin=np.zeros (10)
    st_dev_byN=[0]
    all_N=[0]
    if4=0
    for t in range (1, T):
        
        j=0
        while j<N:
            x=random.randint(0, 9)
            if if4==1:
                fin [x]+=1
                j+=1
            if4=0
            if x==4:
                if4=1   
            
        st_dev_byN.append(statistics.stdev(fin)/(N*t))
        all_N.append(1/math.sqrt(N*t))
    finst=np.vstack([finst,st_dev_byN])

for t in range (0,len(finst)):
    st_dev_byN[t]=np.average(finst[t])

plt.scatter(np.log (st_dev_byN), np.log (all_N))
plt.show ()


RNG = pd.DataFrame({'1/sqrt (N)':np.log (all_N), 'stdev/N':np.log (st_dev_byN)}) #for the data
datatoexcel = pd.ExcelWriter('RNG after4 1k rounds each 1k times.xlsx')
RNG.to_excel(datatoexcel)
datatoexcel.save()


print("--- %s seconds ---" % (time.time() - start_time)) #runtime