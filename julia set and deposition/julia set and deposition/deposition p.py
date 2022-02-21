# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:52:26 2021

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
    

t=0
while t<T:
    i=0
    while i<n:
        fin [randint (0,l-1)]+=1
        i+=1
    finfin=np.vstack([finfin, fin])
    t+=1
    


count=0
for count in range(0,T):
    w.append (math.sqrt(statistics.variance(finfin [count])))
    count+=1

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
count=0
for count in range(0,T):
    avh.append(sum (finfin[count])/l)
    count+=1

count=0
for count in range(0,T):
    betha.append(np.log(w[count])/np.log(count))
    count+=1
'''

plt.scatter(time, w)
#plt.scatter(time, betha)
betha_final = sum (betha[4000:5000])/1000

plt.show()