# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 18:13:15 2021

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

l=40
finper=[]
def col_changer(col, i,j, colour,num):
    colp= col
    for ip in range (0,i+1):
        for jp in range (0,l):
            if col [ip][jp]==colour:
                colp [ip][jp]=num
    return colp

perarr=[]
parr=[]
fin_avg_gyr=[]
for pcount in range (0,20):
    p=pcount/20
    finper=[]
    gyr=[]
    for count in range (0,10):
        
        space = np.zeros ((l,l)) #array of the space for on and off
        col = np.zeros ((l,l)) #array foe colours
        
        
        
            
        
        for i in range (0,l):
            for j in range (0,l):
                if random.random()<=p:
                    space [i][j]=1
        
        num =10 #the number that will be the colour identifier
        curr=0 #shows if the last pixel was on or off
        for i in range (0,l):
            for j in range (0,l):
                if i==0:#colouring first row
                    if space [i][j]==1: 
                        if curr==0:
                            num+=1
                            curr=1
                        col [i][j]=num
                    if space [i][j]==0:
                            curr=0
                    num_of_first=num
                
                            
                elif space [i][j]==1:
                    if curr==0:
                        num+=1
                        curr=1
                    col [i][j]=num
                    if space [i-1][j]==1:
                        col = col_changer(col, i,j, col [i-1][j],num)
                
                elif space [i][j]==0:
                        curr=0
            curr=0 #to make sure number of pixels on the next row wont be the same is this if not connected afterwards
        
        inf_col=[]
        per=0 # now i'll check if any pixel on left has the same colour with any on right
        for j1 in range (0,l):
            for j2 in range (0,l):
                if col [0][j1]==col [l-1][j2] and col [0][j1]!=0:
                    per=1
                    if not col [0][j1] in inf_col:
                        inf_col.append(col [l-1][j2])
        
        allcol=[]
        allnum=0
        
        for houserow in col:
            for house in houserow:
                x=[]
                y=[]
                num=0
                if house !=0 and house not in inf_col and house not in allcol:
                    allcol.append(house)
                    for i in range (0,l):
                        for j in range (0,l):
                            if col [i][j]==house:
                                x.append (i)
                                y.append (j)
                                col [i][j]=0
                                num+=1
                    if num>1:
                        gyr.append((statistics.variance(x)+statistics.variance(y))**.5)
                        allnum+=1
                    '''if num==1:
                        gyr.append(0)
                        allnum+=1'''
        if allnum==0:
            gyr.append(0)
    fin_avg_gyr.append(np.average(gyr))
    
    perarr.append (np.mean(finper))
    parr.append (p)
    
avglen = pd.DataFrame({'probablity':parr, 'per_prob':fin_avg_gyr}) #for the data
datatoexcel = pd.ExcelWriter('3avgxi40.xlsx')

avglen.to_excel(datatoexcel)

datatoexcel.save()
'''
for i in range (0,l): #to draw the mesh
    for j in range (0,l):
        random.seed(col[i][j])
        if col [i][j]!=0:
            plt.scatter(i, j, marker="s", c= (random.random(),random.random(),random.random()), s=400)

plt.show()

per_prob = pd.DataFrame({'probablity':parr, 'perculation':perarr}) #for the data
datatoexcel = pd.ExcelWriter('perprob.xlsx')

per_prob.to_excel(datatoexcel)

datatoexcel.save()
'''
print("--- %s seconds ---" % (time.time() - start_time)) #runtime