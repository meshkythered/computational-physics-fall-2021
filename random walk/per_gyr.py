# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:53:48 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
import random
import numpy as np
import statistics
import pandas as pd
import time
start_time = time.time()

T=70 #growing times
p=.5
l=T*2+2 #length of lattice
def mainfun (final, newx,newy,allx,ally): #there's not much fun :)), just the main function
    new_len=0 #this will count the number of units added in this growth stage
    newxp=[] #Xs of them
    newyp=[] #Ys of them
    for num in range (0,len(newx)): #newx and newy were the coordinations of last phase growth units
        x=newx[num]#growing from the last generation
        y=newy[num]
        for dx in range (0,2): #right snd left of each house
            if final [x-1+dx*2][y] !=1:
                if random.random()<=p and final [x-1+dx*2][y]!=-1: #randomly turns on if not blocked
                    final [x-1+dx*2][y]=1
                    newxp.append(x-1+dx*2)
                    newyp.append(y)
                    allx.append(x-1+dx*2)
                    ally.append(y)
                    new_len+=1
                elif random.random()>p:
                    final [x-1+dx*2][y]=-1 #blocks the house
                
        for dy in range (0,2): #up and down of each house
            if final [x][y-1+dy*2] !=1:
                if random.random()<=p and final [x][y-1+dy*2]!=-1:
                    final [x][y-1+dy*2]=1
                    newxp.append(x)
                    newyp.append(y-1+dy*2)
                    allx.append(x)
                    ally.append(y-1+dy*2)
                    new_len+=1
                elif random.random()>p:
                    final [x][y-1+dy*2]=-1
    return (final, newxp,newyp, new_len)

gyr=[]
sur=[]
t_arr=np.arange(T)
len_count=[]
for count in range (0,20): #ensembles
    all_num=0
    newx=[]
    newy=[]
    main = np.zeros ((l,l))
    main [T][T]=1
    newx.append(T)
    newy.append(T)
    allx=ally=newx
    for t in range (0,T):
        if count==0:
            plt.scatter(newx, newy, marker="s", c= (1-t/T,0,0), s=30)
        main,newx,newy,newlen=mainfun (main, newx,newy,allx,ally)
        if newlen==0:# if no new dots were added gets it out of cycle
            break
        all_num+=newlen
        if len(gyr)==t: #adds a new row if no last shape reached this level
            sur.append([])
            gyr.append([])
        gyr [t].append([(statistics.variance(allx)+statistics.variance(ally))**.5])
        sur [t].append(all_num)

plt.show()
t_arr=np.arange(len(gyr))
fin_gyr=[] #avg of all
fin_sur=[]
for gyrcount in range(0,len(gyr)):
    fin_sur.append (np.average(sur[gyrcount]))
    fin_gyr.append (np.average(gyr[gyrcount]))
pergyr = pd.DataFrame({'times':t_arr, 'gyr_r':fin_gyr, 'surface': fin_sur})
datatoexcel = pd.ExcelWriter('per_gyr_p5.xlsx')

pergyr.to_excel(datatoexcel)

datatoexcel.save()


print("--- %s seconds ---" % (time.time() - start_time)) #runtime