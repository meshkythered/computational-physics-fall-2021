# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:24:05 2021

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

def g(x):
    sig=1
    return( math.e**(-x**2/(2*sig**2)))

n=100 #how many times the game shall be played before reading th coordinate again
def generate (size , step):
    x=0
    acc=0 #acception rate
    allnum=np.zeros (n*size) #all numbers
    num=np.zeros (size) #random numbers
    
    for i in range (0,size):
        for j in range (0,n):
            x2= x+ step*(1-2*random.random()) #new x
            if g(x2)/g(x)>random.random():
                x=x2
                acc+=1
            allnum[i*n+j]=x
        num[i]=x
    acc_rate=acc/(n*size)
    return (acc_rate, num, allnum)

'''
#to check working
step=3
a,num,b= generate(10000, step)
minn=np.amin(num)
maxn=np.amax(num)
lenn=int(maxn*10)- int(minn*10)
space=np.arange(int(minn*10),int(maxn*10)+1)/10
dist=np.zeros (lenn+1)
for number in num:
    dist [int(number*10)-int(minn*10)]+=1

plt.scatter (space,dist)
plt.title('step = %s' %step)
plt.show()
plt.savefig('step = %s' %step)

'''
'''
#to find steps for accept rates
acc_rate=np.zeros (161)
for count in range (4,161):
    acc, num, allnum=generate (1000 , count/10)
    acc_rate[count]=acc

X=np.arange(0,161)/10
plt.scatter(X, acc_rate)    
plt.grid()
plt.show()
'''
''' 
step   acc_rate
.50     .9
1.03    .8
1.58    .7
2.20    .6
2.94    .5
3.89    .4
5.30    .3
7.97    .2
15.9    .1
'''
steps=[15.9,7.97,5.3,3.89,2.94,2.2,1.58,1.03,.5]


def corlen (step, size):
    a,num,b=generate (size , step)
    cor_arr=[] #saves cordinations per j
    for j in  range (0,size):
        add=0
        for i in range (0,size-j):
            add+=abs(num[i]*num[i+j])
        add/=(size-j)
        cor_arr.append((add-np.mean(num)**2)/statistics.variance(num))
    print (cor_arr)
    lenn=0
    for cor in cor_arr:
        if cor < math.e**(-1):
            lenn+=1
    return (lenn)

fin_cor_arr=[]
size=30
for step in steps:
    fin_cor_arr.append(corlen(step,size))

