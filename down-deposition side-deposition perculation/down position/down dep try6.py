# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:25:32 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
from random import randint
import numpy as np
import statistics
import pandas as pd
import math
import time
start_time = time.time()

finw=[]
for k in range (9,27):
    

    T=20 #how many times
    l=int (2**(k/3)) #length
    n=10*l #dots per times
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
        
    
    t=0
    while t<T:
        i=0
        while i<n:
            x=np.random.randint(l-1)
            x1= (x-1+l)%l
            x2= x
            x3= (x+1)%l
            y= min(fin[x1], fin[x2],fin[x3])
            if y==fin[x2]:
                fin[x2]+=1
            elif y==fin[x1]and fin[x3]!=y:
                fin[x1]+=1
            elif y==fin[x3]and fin[x1]!=y:
                fin[x3]+=1
            else:
                k=randint(0,1)
                if k==0:
                    fin[x3]+=1
                if k ==1:
                    fin[x1]+=1
            i+=1
        w.append (statistics.variance(fin))
        #avh.append(sum (fin)/l)
        #betha.append(np.log(w[t])/np.log(t))
        finfin=np.vstack([finfin, fin])
        t+=1
    finw.append(np.average(w[400:600]))

'''

for count in range(0,T):#the deposition chart itself
    plt.bar(X, finfin [T-count], color=(count/T,count/T,0))



plt.scatter(np.log(time), np.log (w))
#plt.scatter(time, betha)
#betha_final = sum (betha[4000:5000])/1000


plt.show()
'''
''''''
count=0 #the deposition chart itself
for j in range(1,T):
    plt.figure()
    plt.ylim(0,max(finfin[T]))
    for count in range(0,j):
        plt.bar(X, finfin [j-count], color=((T-j+count)/T,(T-j+count)/T,0))
        count+=1
        plt.title('deposition %s times' %j)
        plt.savefig('deposition %s times' %j)
'''
K=np.arange(9,27)
varriance_side = pd.DataFrame({'length log':K, 'variance':np.log (finw)/np.log(2)*3})
datatoexcel = pd.ExcelWriter('alpha4.xlsx')

varriance_side.to_excel(datatoexcel)

datatoexcel.save()'''
