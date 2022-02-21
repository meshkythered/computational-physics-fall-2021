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


N=19
l=2*N+1
latt = np.zeros ((l,l))
latt [N][N]=1
x,y=N,N
path_vs_n=np.zeros (N)

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



t=0 #this will later if the random walk took it's fisrt turn

#the last parts of ifs down this function will set that the first move will be right and if it wants to turn at any point that will be up
def main (x,y,space,n,t):
    path_vs_n[n]+=1
    space [x][y]=1
    if neigh(x, y,space)==4 or n>=N-1:
        '''plt.figure()
        plt.imshow(space)
        #plt.show()'''
        return()
    
    spacep=np.copy(space)
    if space [x+1][y]==0 :
        main (x+1,y,spacep,n+1,t)
        
    spacep=np.copy(space)
    if space [x-1][y]==0 and t!=0:
        main (x-1,y,spacep,n+1,t)
        
    spacep=np.copy(space)
    if space [x][y+1]==0 and n!=0:
        main (x,y+1,spacep,n+1,t+1)#when t isn't 0 anymore, other moves will be allowed too
    
    spacep=np.copy(space)
    if space [x][y-1]==0 and t!=0:
        main (x,y-1,spacep,n+1,t)


main (x,y,latt,0,t)
for path in path_vs_n:
    path= path*8-4


path_vs_n = pd.DataFrame({'paths with each n':path_vs_n}) #for the data
datatoexcel = pd.ExcelWriter('path_vs_n19.xlsx')

path_vs_n.to_excel(datatoexcel)

datatoexcel.save()
print("--- %s seconds ---" % (time.time() - start_time)) #runtime