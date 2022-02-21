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

l=20        
def col_changer(col, i,j, colour,num):
    colp= col
    for ip in range (0,i+1):
        for jp in range (0,l):
            if col [ip][jp]==colour:
                colp [ip][jp]=num
    return colp

perarr=[]# array of perculations
parr=[]# array of probablities
fin_avg_gyr=[] #avg Gyration radius
con_prob=[]#the probablity of being connected to infinite branch
for pcount in range (0,1):
    p=.5#pcount/20
    finper=[]#saves the perculations to get an ensemble avg afterwards
    avg_gyr =[]#saves the avg gyr each try to get an ensemble avg afterwards
    connection=[]#saves the probablity of being connected to infinite branch each try to get an ensemble avg afterwards
    gyr=[]
    for count in range (0,6): #tries for being able to use ensemble average
        vbrff=int(l*l/2)+11 #maximum number of colours there could be
        counterx=np.zeros (vbrff) # counterx[a]= x of houses on a branch with colour a
        countery=np.zeros (vbrff) # counterx[a]= x of houses on a branch with colour a
        non_0_counterx=[]# only contains the non-zero branch x
        non_0_countery=[]
        inf_col=[] #colours of the infinite branches
        space = np.zeros ((l,l)) #array of the space for on and off
        col = np.zeros ((l,l)) #array foe colours
        on=0 #all ON houses
        
        
        
        
            
        
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
                    if not col [0][j1] in inf_col:
                        inf_col.append(col [l-1][j2])
                    
      
        
        '''
        #for connection probablity
        conn=0 #connected houses
        for houserow in col: #to count connected houses
            for house in houserow:
                if house in inf_col:#knows if house is connected to one of infinite branches
                    conn+=1


        '''
        alcol=[]
        allnum=0
        for houserow in col:
            for house in houserow:
                x=[]
                y=[]
                num=0
                if house !=0 and house not in inf_col and house not in alcol:
                    alcol.append(house)
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
        
        '''
        #for avg length
        for i in range (0,l): #to form counter matrix 
            for j in range (0,l): 
                if col [i][j]!=0:
                    if not col [i][j] in inf_col:#checks if x is not connected to one of infinite branches
                        counterx [col [i][j]].append (int(i))
                        countery [col [i][j]].append (int(j))
        
        for kooft in range (0,len(counterx)):
            if counterx[kooft].size >1:
                non_0_counterx.append(counterx[kooft] [1:len (counterx[kooft])]) #because we used "extend" the first x is unchanged zero
                non_0_countery.append(countery [kooft][1:len (countery[kooft])])
        
        
        for kooft in range (0, len(non_0_counterx)):
            gyr.append((statistics.variance(non_0_counterx [kooft])+statistics.variance(non_0_countery [kooft]))**.5)
        #finper.append (per) #saves the perculations to get an avg afterwards'''
        '''if on==0:
            connection.append(0)
        else: 
            connection.append(conn/on)'''
    fin_avg_gyr.append(np.average(gyr))
    #con_prob.append(np.average(connection))
        
    #perarr.append (np.average(finper))
    parr.append (p)
'''
for i in range (0,l): #to draw the mesh
    for j in range (0,l):
        random.seed(col[i][j])
        if col [i][j]!=0:
            plt.scatter(i, j, marker="s", c= (random.random(),random.random(),random.random()), s=400)

plt.show()
'''
avglen = pd.DataFrame({'probablity':parr, 'per_prob':fin_avg_gyr}) #for the data
datatoexcel = pd.ExcelWriter('avgxi10.xlsx')

avglen.to_excel(datatoexcel)

datatoexcel.save()

print("--- %s seconds ---" % (time.time() - start_time)) #runtime