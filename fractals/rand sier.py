# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:46:33 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from random import randint
  
'''            (0,0)=1



(-1,-3**.5)=2                (1,-3**.5)=3
'''
final_x=[]
final_y=[]
def f1 (x,y): #upper function
    x1=x/2
    y1=y/2
    return (x1,y1)

def f2 (x,y): #down left function
    x2=x/2 - 0.5
    y2=y/2 - 3**0.5/2
    return (x2,y2)

def f3 (x,y): #down right function
    x3=x/2 + 0.5
    y3=y/2 - 3**0.5/2
    return (x3,y3)

for i in range (1,1000000):
    a= randint(1,3) #which point to start from
    x=0
    y=0
    if (a==2):
        x= -1
        y= -3**.5
    if (a==3):
        x= 1
        y= -3**.5
    
    b= randint(1,100) # how many times functions should be applied
    for j in range (1,b):
        b=randint(1,3) #what function will be applied each time
        if b==1:
            x,y=f1(x,y)
        if b==2:
            x,y=f2(x,y)
        if b==3:
            x,y=f3(x,y)
    
    final_x.append (x)
    final_y.append (y)
    if i in [30,100,300,1000,3000,10000,30000,999999]:
        plt.figure()
        plt.scatter(final_x, final_y, .02, edgecolor ='green')
        plt.title ('rand sierpinsky %s dots'%i)
        plt.savefig('%s dots'%i)

  
plt.show()   