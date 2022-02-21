# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:52:46 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
from random import randint
import numpy as np
import statistics
import math

T=10 #how many times
n=2000 #dots per times
l=200 #length
fin = np.zeros (l) #main final functionT gets the processes
finfin =np.zeros (l) #saves fin each time
X=[] #a simple array used only for x coordiantion when printing
time=[] #a simple array used only for t coordiantion when printing
w=[] #array of variances
avh=[]
betha= []


for count in range (0,l):
    X.append(count)
    count+=1

count=0
for count in range (0,T):
    time.append(count)
    count+=1
    
    
i=0
for j in range (0,T):
    for i in range (0,n):
        x= randint (0,l-1)
    
    
        if x==l-1:
            if fin [x]<= fin [x-1]:
                fin [x]+=1
            else: 
                fin [x-1]+=1
        elif x==0:
            if fin [x]<= fin [x+1]:
                fin [x]+=1
            else: 
                fin [x+1]+=1
    
    
    
    
        if x!=0 and x!=l-1:
            y= min(fin[x], fin[x-1],fin[x+1])
            if y==fin[x]:
                fin[x]+=1
            elif y==fin[x-1]and fin[x+1]!=y:
                fin[x-1]+=1
            elif y==fin[x+1]and fin[x-1]!=y:
                fin[x+1]+=1
            else:
                k=randint(0,1)
                if k==0:
                    fin[x+1]+=1
                if k ==1:
                    fin[x-1]+=1
    finfin=np.vstack([finfin, fin])


for count in range(0,T):#the deposition chart itself
    plt.bar(X, finfin [T-count], color=(count/T,count/T,0))

'''

count=0
for count in range(0,T):
    w.append (math.sqrt(statistics.variance(finfin [count])))
    count+=1


count=0
for count in range(0,T):
    avh.append(sum (finfin[count])/l)
    count+=1

count=0
for count in range(0,T):
    betha.append(np.log(w[count])/np.log(count))
    count+=1

plt.scatter(time, w)
#plt.scatter(time, betha)
#betha_final = sum (betha[4000:5000])/1000

'''
plt.show()

plt.show()