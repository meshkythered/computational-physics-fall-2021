# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:06:10 2021

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


N=20
l=2*N+1
latt = np.zeros ((l,l))
latt [N][N]=1
x,y=N,N
L_vs_n=np.zeros (N)

def neigh (x,y,space):#knows if it has a neighbor and how many
    nei=0
    if space [x-1][y]==1:
        nei+=1
    if space [x+1][y]==1:
        nei+=1
    if space [x][y-1]==1:
        nei+=1
    if space [x][y+1]==1:
        nei+=1
    return (nei)

def main (x,y,space,n):
    L_vs_n[n]+=1
    space [x][y]=1
    if neigh(x, y,space)==4 or n>=N-1:
        '''plt.figure()
        plt.imshow(space)
        #plt.show()'''
        return()
    
    spacep=np.copy(space)
    if space [x+1][y]==0:
        main (x+1,y,spacep,n+1)
        
    spacep=np.copy(space)
    if space [x-1][y]==0:
        main (x-1,y,spacep,n+1)
        
    spacep=np.copy(space)
    if space [x][y+1]==0:
        main (x,y+1,spacep,n+1)
    
    spacep=np.copy(space)
    if space [x][y-1]==0:
        main (x,y-1,spacep,n+1)

path_vs_n = pd.DataFrame({'paths with each n':L_vs_n}) #for the data
datatoexcel = pd.ExcelWriter('path_vs_n19.xlsx')

path_vs_n.to_excel(datatoexcel)

datatoexcel.save()
main (x,y,latt,0)
print("--- %s seconds ---" % (time.time() - start_time)) #runtime