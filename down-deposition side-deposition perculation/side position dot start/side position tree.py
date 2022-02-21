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

T=15 #how many times
n=2000 #dots per times
l=200 #length
fin = np.zeros (l) #main final function, gets the processes
fin = fin -1000
fin [100]=0
dotsx =[] #saves the dot each drop
dotsy =[] #saves the dot each drop
finfinx =[] #saves dots matrix each time
finfiny =[] #saves dots matrix each time
X=[] #a simple array used only for x coordiantion when printing
time=[] #a simple array used only for t coordiantion when printing
w=[] #array of variances
avh=[]
betha= []


for count in range (0,l):
    X.append(count)
    count+=1
lenarr=[] #array of lengths
count=0
for count in range (0,T):
    time.append(count)
    count+=1
    
el_ultimo=100 #the x of the last dot(s) on the right
el_primero=100 ##the x of the last dot(s) on the left
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
        if y>=0:
            dotsx.append (x)
            dotsy.append (y)
            fin [x]=y
            if x>el_ultimo:
                el_ultimo=x
            if x<el_primero:
                el_primero=x
        i+=1
    
    lenarr.append(el_ultimo- el_primero)
    t+=1

for i in range (1,T):
    plt.figure(dpi=100)
    plt.xlim(min(dotsx),max(dotsx))
    plt.ylim(min(dotsy),max(dotsy))
    for count in range(0,i):
        plt.scatter(2*dotsx [n*count :n*count+n-1],2*dotsy [n*count :n*count+n-1], s=.5, c=(.9-count/T,.9-count/T*.8,1))
        plt.title('side psition tree %s times' %i)
        plt.savefig('side position tree %s times' %i)

'''plt.scatter(time,lenarr)
for count in range(0,T):
    w.append (math.sqrt(statistics.variance(finfin [count])))
    count+=1

#the shape itself
for count in range(0,T):
    plt.scatter(finfinx [T-count-1],finfiny [T-count-1],10, c=(1-count/T*.4,1-count/T*.3,1))'''

'''
for count in range(0,T):
    avh.append(sum (finfin[count])/l)
    count+=1


for count in range(0,T):
    betha.append(np.log(w[count])/np.log(count))
    count+=1'''

#plt.scatter(time, w)
#plt.scatter(time, betha)
#betha_final = sum (betha[4000:5000])/1000

plt.show()