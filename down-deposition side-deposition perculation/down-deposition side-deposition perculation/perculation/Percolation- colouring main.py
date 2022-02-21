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

l=100
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
for pcount in range (0,21):
    p=pcount/20
    finper=[]
    for count in range (0,5):
        
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
        
        
        per=0 # now i'll check if any pixel on left has the same colour with any on right
        for j1 in range (0,l):
            for j2 in range (0,l):
                if col [0][j1]==col [l-1][j2] and col [0][j1]!=0:
                    per=1

        finper.append (per) #saves the perculations to get an avg afterwards
    perarr.append (np.mean(finper))
    parr.append (p)
'''
for i in range (0,l): #to draw the mesh
    for j in range (0,l):
        random.seed(col[i][j])
        if col [i][j]!=0:
            plt.scatter(i, j, marker="s", c= (random.random(),random.random(),random.random()), s=400)

plt.show()
'''
per_prob = pd.DataFrame({'probablity':parr, 'perculation':perarr}) #for the data
datatoexcel = pd.ExcelWriter('perprob100.xlsx')

per_prob.to_excel(datatoexcel)

datatoexcel.save()

print("--- %s seconds ---" % (time.time() - start_time)) #runtime