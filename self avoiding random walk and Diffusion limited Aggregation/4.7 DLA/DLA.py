# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:34:26 2021

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
#from images2gif import writeGif
plt.figure(figsize=(10,7.5))
T=60
lx=200
ly=150
p=.25 #probablity of moving forward, right
q=.25 #probablity of moving up
space = np.zeros ((lx,ly)) 
for i in range (0,lx-1): #to put the seed
    space[i][0]=1
    plt.scatter(i, 0,c= (0,0,0))

def move (x,y):
    if np.random.random()<.5: #moves in x direction
        if np.random.random()<.5:
            if x==lx-1:#periodic borders
                x=0
            else:
                x+=1
        else:
            if x==0:
                x=lx-1
            else :
                x-=1
    else: #moves in y direction
        if np.random.random()<.5:
            if y==ly-1:
                x=random.randint(0, lx-1) #starts a new dot
                y=ly
            else:
                y+=1
        else:
            y-=1
    if y>=ly:
        y=ly-1
    return (x,y)

def neigh (x,y):#knows if it has a neighbor
    nei=0
    if x==0:
        if space [lx-1][y]==1:
            nei=1
    else:
        if space [x-1][y]==1:
            nei=1
    if x==lx-1:
        if space [0][y]==1:
            nei=1
    else:
        if space [x+1][y]==1:
            nei=1
    if space [x][y-1]==1:
        nei=1
    if y==ly-1:
        nei=0
    elif space [x][y+1]==1:
        nei=1
    return (nei)


plt.ylim([0, ly])
n=3000
for i in range (0,n):
    nei=0
    x=random.randint(0, lx-1)
    y=ly
    while nei==0:
        x,y= move (x,y)
        nei= neigh (x,y)
    if nei==1:
        space [x][y]=1
        plt.scatter(x, y,c= (i/n,0,0))
    if i%500==499:
        plt.title('after %s falls'%(i+1))        
        plt.savefig('DLA %s.png'%(i+1))




#writeGif("2d.gif", images, duration=0.2)
print("--- %s seconds ---" % (time.time() - start_time)) #runtime