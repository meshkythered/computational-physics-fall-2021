# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:59:22 2021

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

l=60 #length of road :)
p=1 #probablity of moving forward, right
POS= np.arange(-10,11) #a simple for exporting data
right_fall_prob=[] # right_fall_prob[t]= probablity of falling down from right side on time=t
left_fall_prob=[]
fall_time=[]#a simple array for exporting data
def mainfun (pr_arr,t): #
    new=np.zeros (l)
    for x in range (1,l-1):
        new [x]= pr_arr [x-1]*p+pr_arr [x+1]*(1-p)
    
    new [0]=pr_arr [1]*(1-p)
    #left_fall_prob.append (pr_arr[0]*(1-p))
    
    new [l-1]=pr_arr [l-2]*p
    #right_fall_prob.append (pr_arr[l-1]*p)
    #fall_time.append(t)
    print ('boo')
    return (new)

main=np.zeros (l)

t_arr=[0]
c=.371 #tells us when to assume that the walker has fallen in the main while
liveper=[1]
t_per_pos=[]
avgx=[]
sigma=[]
main=np.zeros (l)
main [30]=1
for t in range (0,20):
    t=0
    main=mainfun(main, t)
    #t_arr.append(count)
        #liveper.append(np.sum(main))
    x=[]
    x2=[]
    for c in range (0,60):
        if main [c]!=0:
            x.append(c*main[c])
            x2.append(c**2*main[c])
        
    t_arr.append(t)
    avgx.append(np.average(x))
    sigma.append(np.average(x2)-np.average(x)**2)

'''
plt.scatter(X,main)
plt.show()
print(right_fall_prob)

avglifetime = pd.DataFrame({'time':t_arr, 'avgx':avgx, 'sigma': sigma}) #for the data
datatoexcel = pd.ExcelWriter('avgx & sigma p5.xlsx')

avglifetime.to_excel(datatoexcel)

datatoexcel.save()'''
print("--- %s seconds ---" % (time.time() - start_time)) #runtime