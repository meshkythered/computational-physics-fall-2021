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

l=21
p=.6
t=0
T=100
avgx=[]
sigma=[]
X=np.arange (l)
right_fall_prob=[]
right_fall_time=[]
left_fall_prob=[]
left_fall_time=[]
def mainfun (pr_arr,t,p):
    new=np.zeros (l)
    new [int(l/2)]=1
    for x in range (1,l-1):
        new [x]= pr_arr [x-1]*p+pr_arr [x+1]*(1-p)
    
    new [0]=pr_arr [1]*(1-p)
    left_fall_prob.append (pr_arr[0]*(1-p))
    left_fall_time.append(t)
    
    new [l-1]=pr_arr [l-2]*p
    right_fall_prob.append (pr_arr[l-1]*p)
    right_fall_time.append(t)
    return (new)

main=np.zeros (l)

t_arr=[0]

liveper=[1]
t_per_pos=[]
for pos in range (0,21):
    main [pos]=1
    count=0
    while np.sum(main)>.0001:
        main=mainfun(main, t)
        #t_arr.append(count)
        #liveper.append(np.sum(main))
        count+=1
        x_arr=[]
        x2_arr=[]
        for alpha in range (0,l):
            x_arr.append((alpha-l/2)*main[alpha])
            x2_arr.append((alpha-l/2)**2*main[alpha])
        avgx.append(np.average(x_arr))
        sigma.append(np.average(x2_arr)-np.average(x_arr)**2)
    t_per_pos.append(count)
POS= np.arange(-10,11)

'''
plt.scatter(X,main)
plt.show()
print(right_fall_prob)
'''
avglifetime = pd.DataFrame({'start pos':POS, 'avg lifetime':t_per_pos}) #for the data
datatoexcel = pd.ExcelWriter('avg lifetime efficient +_+ per starting point.xlsx')

avglifetime.to_excel(datatoexcel)

datatoexcel.save()
print("--- %s seconds ---" % (time.time() - start_time)) #runtime