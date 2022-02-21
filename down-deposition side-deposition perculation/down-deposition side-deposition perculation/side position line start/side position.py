# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:25:32 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
from random import randint
import numpy as np
import statistics
import math
import pandas as pd
fin_avh=[]
alphw=[]
finw=[]
for k in range (9,27):
    print ('dam')

    T=15 #how many times
    l=int (2**(k/3)) #length
    n=10*l #dots per times
    finw=np.zeros (T)
    for lalalalalala in range (0,10):
        print ('boom')
        fin = np.zeros (l) #main final function, gets the processes
        dotsx =[] #saves the dot each drop
        dotsy =[] #saves the dot each drop
        finfinx =[] #saves dots matrix each time
        finfiny =[] #saves dots matrix each time
        X=np.arange(l) #a simple array used only for x coordiantion when printing
        time=np.arange(T) #a simple array used only for t coordiantion when printing
        w=[] #array of variances each time
        avh=[]
        
        
        t=0
        while t<T:
            i=0
            while i<n:
                x=randint (0,l-1)
                if x==0:
                    y= max(fin[x], fin[x+1])
                elif x==l-1:
                    y= max(fin[x], fin[x-1])
                elif x!=0 and x!=l-1:
                    y= max(fin[x], fin[x+1], fin[x-1])
                if y==fin [x]:
                    y+=1
                dotsx.append (x)
                dotsy.append (y)
                fin [x]=y
                i+=1
            finfinx.append( dotsx)
            finfiny.append( dotsy)
            w.append (statistics.variance(fin))
            avh.append(np.average (fin))
            t+=1
        finw+=w
    finw=finw/k
    alphw.append(np.average(finw[300:400]))


#the shape itself
for i in range (1,T):
    plt.figure()
    plt.xlim(min(dotsx),max(dotsx))
    plt.ylim(min(dotsy),max(dotsy))
    for count in range(0,i):
        plt.scatter(2*dotsx [n*count :n*count+n-1],2*dotsy [n*count :n*count+n-1], s=1, c=(.9-count/T,.9-count/T*.8,1))
        plt.title('side psition %s times' %i)
        plt.savefig('side position %s times' %i)
'''


plt.scatter(time, finw)
#plt.scatter(time, avh)

plt.show()

K=np.arange(9,27)
var_side = pd.DataFrame({'time':np.log(K), 'variance':np.log (alphw)/np.log(2)*3})
datatoexcel = pd.ExcelWriter('var6_alp_side.xlsx')

var_side.to_excel(datatoexcel)

datatoexcel.save()'''