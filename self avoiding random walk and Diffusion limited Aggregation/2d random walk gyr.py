# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:55:41 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
import random
import numpy as np
import statistics
import math
import pandas as pd
import time
from PIL import Image
start_time = time.time()
#from images2gif import writeGif

T=60
l=2*T+1 #length of road :)
p=.25 #probablity of moving forward, right
q=.25 #probablity of moving up
space = np.zeros ((l,l)) 
space [int(l/2)][int(l/2)]=1
def mainfun (pr_arr,t): #gets the space through each round
    new = np.zeros ((l,l)) 
    for x in range (1,l-1):
        for y in range (1,l-1):
            new [x][y]= pr_arr [x-1][y]*p+pr_arr [x+1][y]*(.5-p)+pr_arr [x][y-1]*q+pr_arr [x][y+1]*(.5-q)
    
    #i wont set the code for boroders, instead i set the borders larger than times tried
    '''
    new [0]=pr_arr [1]*(1-p)
    #left_fall_prob.append (pr_arr[0]*(1-p))
    
    new [l-1]=pr_arr [l-2]*p
    #right_fall_prob.append (pr_arr[l-1]*p)
    #fall_time.append(t)''' 
    return (new)


t_arr=[0]
c=.371 #tells us when to assume that the walker has fallen in the main while
liveper=[1]
t_per_pos=[]
avgx=[]
gyr=[0]
images=[]

for t in range (1,T):
    space=mainfun(space, t)
    #t_arr.append(count)
        #liveper.append(np.sum(main))
    r=[]
    r2=[]
    for xc in range (0,l-1):
        for yc in range (0,l-1):
            if space [xc][yc]!=0:
                r2.append(((xc-T)**2+(yc-T)**2)*space[xc][yc])
    plt.figure()            
    im = plt.imshow(space, cmap=plt.cm.RdBu,extent=(0, l, 0, l), interpolation='bilinear')
    plt.colorbar(im);
    plt.title('2d random walk %s round.png'%t)
    '''
    im = im.save("2d %s.jpg" %t)
    images.append(im) '''           
    plt.savefig('2d %s.png'%t)

    t_arr.append(t)
    gyr.append(np.sum(r2)**.5)

plt.figure()



'''
gyr_vs_time_2d = pd.DataFrame({'time':t_arr, 'gyr':gyr}) #for the data
datatoexcel = pd.ExcelWriter('gyr_vs_time_2d.xlsx')

gyr_vs_time_2d.to_excel(datatoexcel)

datatoexcel.save()
'''
#writeGif("2d.gif", images, duration=0.2)
print("--- %s seconds ---" % (time.time() - start_time)) #runtime