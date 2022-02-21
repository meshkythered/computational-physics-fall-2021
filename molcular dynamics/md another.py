# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:25:48 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
start_time = time.time()

T=.8
h=.001
n=100
mean_v2=np.zeros(int(T/h))
plenajon=np.zeros(int(T/h))

Time=[]

m=1
k=1.4*10**-23
X=Y=1000000
ep=100
vmax=X*2**.5
sig=(X*Y/n)**.5*2
x=[]
y=[]
lefts=[]

for dx in np.arange(X/22,X/22*10+1,X/22):
    for dy in np.arange(Y/11,Y/11*10+1,Y/11):
        x.append(dx)
        y.append(dy)
#x=np.random.rand (n)*X
#y=np.random.rand (n)*Y
vx=vmax*(.5-np.random.rand (n))*2
vy=vmax*(.5-np.random.rand (n))*2
ax=np.zeros (n)
ay=np.zeros (n)

def Tcal (mean_v2):
    return (m*mean_v2/2/k)

def P (T):
    return(n*k*T/X/Y)

def plenjon(x,y):
    e=0
    
    for j in range (0,n):
        for perx in [-1,0,1]:
            for pery in [-1,0,1]:
                if perx!=0 or pery!=0 or i!=j:
                    d= np.sqrt (dx**2+dy**2)
                    boo=sig/d
                    e+=4*ep*(boo**12-boo**6)
    return(e)

def lenjon (d):
    boo=sig/d
    return (4*ep*(-12*boo**12/d+6*boo**6/d))

def lenajon (i):
    fx=0
    fy=0
    for j in range (0,n):
        for perx in [-1,0,1]:
            for pery in [-1,0,1]:
                if perx!=0 or pery!=0 or i!=j:
                    dx= x[j]-x[i]+perx*X
                    dy= y[j]-y[i]+pery*Y
                    d= np.sqrt (dx**2+dy**2)
                    f=lenjon (d)
                    fx+=f*dx/d
                    fy+=f*dy/d
    return (fx/m,fy/m)

def left (x):
    left=0
    for xx in x:
        if xx<=X/2:
            left+=1
    return (left/len(x))

plt.figure()

for i in range (0,n):
    ax[i],ay[i]=lenajon(i)

for t in range (1, int(T/h)+1):
    plt.figure()
    plt.ylim(0,Y)
    plt.xlim (0,X)
    plt.scatter(x, y)
    #plt.scatter(x[0], y[0], c='red')
    #plt.scatter(x[1], y[1], c='blue')
    tim=(t-1)*h
    plt.title('t=%s'%tim)
    plt.savefig('%s'%(t-1))
    Time.append((t-1)*h)
    mean_v2[t-1]=(np.mean(vx**2+vy**2))
    plenajon[t-1]=( plenjon(x, y))
    lefts.append(left(x))
    for i in range (0,n):
        fx=0
        fy=0
        x[i]=(x[i]+vx[i]*h+ax[i]*h**2/2)%X
        y[i]=(y[i]+vy[i]*h+ay[i]*h**2/2)%Y
        apx,apy=lenajon(i)
        vx[i]+=((apx*ax[i])/abs(apx*ax[i])**.5*h+(apx+ax[i])/2*h)/2
        vy[i]+=((apy*ay[i])/abs(apy*ay[i])**.5*h+(apy+ay[i])/2*h)/2
        ax[i]=apx
        ay[i]=apy

Es= n*m*mean_v2/2 - plenajon
Ts= Tcal(mean_v2)
Ps= P (Ts)


plt.figure()
plt.plot(Time, lefts)
plt.title('left vs time')
plt.xlabel('time')
plt.ylabel('left')
plt.savefig('left vs time h10-3')

plt.figure()
plt.plot(Time, np.log(np.log(mean_v2)))
plt.title('loglogE vs time')
plt.xlabel('time')
plt.ylabel('loglogE')
plt.savefig('loglogE vs time h10-3')

plt.figure()
plt.plot(Time, Ts)
plt.title('logT vs time')
plt.xlabel('time')
plt.ylabel('logT')
plt.savefig('logT vs time h10-3')

plt.figure()
plt.plot(Time, Ps)
plt.title('P vs time')
plt.xlabel('time')
plt.ylabel('P')
plt.savefig('P vs time h10-3')

plt.figure()
plt.plot(Time, Ps)
plt.title('mean v2 vs time')
plt.xlabel('time')
plt.ylabel('mean v2')
plt.savefig('mean v2 vs time h10-3')
print("--- %s seconds ---" % (time.time() - start_time)) #runtime
