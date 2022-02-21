# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:36:39 2021

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
    finfin=[fin]
    for t in range (1, T):
        for j in range (0,N):
            fin [random.randint(0, 9)]+=1
        st_dev_byN.append(statistics.stdev(fin)/(N*t))
        all_N.append(1/math.sqrt(N*t))
        finfin=np.vstack([finfin, fin])
    finst=np.vstack([finst,st_dev_byN])

for t in range (0,len(finst)):
    st_dev_byN[t]=np.average(finst[t])
'''
X=np.arange (10)
for i in range (0,T):
    plt.plot(X, finfin [T-i-1], color= (i/T,0,i/T))
plt.show ()
'''

RNG = pd.DataFrame({'1/sqrt (N)':np.log (all_N), 'stdev/N':np.log (st_dev_byN)}) #for the data
datatoexcel = pd.ExcelWriter('RNG 1k rounds each 1k times.xlsx')
RNG.to_excel(datatoexcel)
datatoexcel.save()


print("--- %s seconds ---" % (time.time() - start_time)) #runtime