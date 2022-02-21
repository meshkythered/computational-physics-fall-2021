# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import time
start_time = time.time()

l=100
J=1
n=5000
ac=40
ensemble=3
def spacemaker (l,beta):
    space= np.random.randint(2, size=(l, l))
    ups=0
    for i in space:
        for j in i:
            if j==1:
                ups+=1
    return (space, ups)


''' calculate correlation'''  #Used Mahani Code
def correlation(array):
    n = len(array) // 10  
    cor = np.zeros(n)
    for i in range(n):
        cor[i]= (  np.dot(  array, np.roll(array, i)  ) / len(array) - np.mean(array) ** 2  ) / np.var(array)
        return cor  

'''correlation of spins on the grid '''   #Used Mahani Code
def spin_cor(S,l):
    cor_lens = np.zeros(l)
    for i in range(l):
        corr_len = correlation(S[i])
        cor_lens[i]= len(corr_len[corr_len > np.exp(-1)]) + 1
    return np.mean(cor_lens)
    

def sp (house):
    return (house*2-1) #0,1 => -1,+1



def En (space):
    energy=0
    for i in range (0,l):
        for j in range (0,l):
            energy-=J* sp(space[i][j])*sp(space[(i-1)%l][j])
            energy-=J* sp(space[i][j])*sp(space[i][(j-1)%l])
    return (energy*2)


def dEn (space, i, j):
    dE= 2 *J* sp(space[i][j])* (sp(space[(i-1)%l][j])+ sp(space[i][(j-1)%l])+sp(space[i][(j+1)%l]) +sp(space[(i+1)%l][j]) )
    return(dE)
    
def comb (ups,l):
    return (math.factorial(l**2)/math.factorial(ups)/math.factorial(l**2-ups))


def step (space , beta,ups):
    i,j=np.random.randint(l) , np.random.randint(l)
    if dEn (space, i , j)<0:
        space [i][j]= 1-space [i][j]
    else:
        if np.random.rand() <  np.exp(-dEn(space, i, j) * beta) :
            space [i][j]= 1-space [i][j]
    if space [i][j]==1:
        ups+=1
    else:
        ups-=1
    return (space,ups)

Beta=np.linspace(0.1, 0.7,ac) 
av_en= np.zeros(ac)
var_en= np.zeros(ac)
av_mag= np.zeros(ac)
var_mag= np.zeros(ac)
Cv = np.zeros(ac)
ksi = np.zeros(ac)

for b in range(0,ac):
    for koofteh in range (0,ensemble):
        space,ups= spacemaker(l, Beta[b])
        ens=[]
        mags=[]
        for count in range (0,n):
            ens.append(En(space))
            mags.append(abs(l**2-ups))
            space, ups=step(space,  Beta[b], ups)
            '''if count%int(n/50)==0 and  b==ac-1 :
                plt.figure()
                plt.imshow(space)
                plt.title("steps=%s"%count)
                plt.savefig("steps=%s"%count)'''
        av_en[b]+=np.mean(ens)/ensemble
        var_en[b]+=np.var(ens)/ensemble
        av_mag[b]+=np.mean(mags)/ensemble
        var_mag[b]+=np.var(mags)/ensemble
        Cv[b]+=np.mean(ens)* Beta[b]**2 /ensemble
        ksi[b]+=np.var(mags)*Beta[b] /ensemble
        

ising  = pd.DataFrame({'Beta': Beta, 'av_en':av_en , 
                       'var_en':var_en, 'av_mag':av_mag ,
                       'var_mag':var_mag ,
                       'Cv':Cv,' ksi': ksi}) #for the data
datatoexcel = pd.ExcelWriter('isingl100.xlsx')
ising.to_excel(datatoexcel)
datatoexcel.save()
print("--- %s seconds ---" % (time.time() - start_time)) #runtime