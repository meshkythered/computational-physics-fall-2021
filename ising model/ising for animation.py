# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
import numpy as np
import statistics
import math
import pandas as pd
import time
start_time = time.time()

l=50
J=1
n=10000
ac=1
ensemble=1
def spacemaker (l,beta):
    space= np.random.randint(2, size=(l, l))
    ups=0
    for i in space:
        for j in i:
            if j==1:
                ups+=1
    return (space, ups)


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

Beta=[10]#Beta=np.linspace(0.1, 0.7,ac) 
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
            if count%int(n/50)==0 and  b==ac-1 :
                plt.figure()
                plt.imshow(space)
                plt.title("steps=%s"%count)
                plt.savefig("steps=%s"%count)
        av_en[b]+=(np.mean(ens))/ensemble
        var_en[b]+=(np.var(ens))/ensemble
        av_mag[b]+=(np.mean(mags))/ensemble
        var_mag[b]+=(np.var(mags))/ensemble

plt.figure()
plt.plot(Beta, av_en)
plt.title("av_en l=%s"%l)
plt.show()
plt.figure()
plt.plot(Beta, av_mag)
plt.title("av_mag l=%s"%l)
plt.show()
plt.figure()
print("--- %s seconds ---" % (time.time() - start_time)) #runtime