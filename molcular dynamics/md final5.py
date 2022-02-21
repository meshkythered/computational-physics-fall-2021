# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:25:48 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import copy
import pandas as pd
start_time = time.time()



T0= 200 #temprature
TTs=[] # Ts for calculating stablity time
Tst=[] # time-stable 
def avg (arr):
    summ=0
    for xxx in arr:
        summ+=xxx
    return(summ/len(arr))

'''
def st_left(lefts,num):
    for i in range (0,len(lefts)-num):
        if abs(np.average(lefts[i:i+num])-.5)<.00001:
            return (i*h+h)
'''

def Tcal (mean_v2): #T out of avg v^2
    return (m*mean_v2*2/k)
    
def P (x,vx,vy): #PA=NKT but for the left side of the container
    leftvx2=[]
    leftvy2=[]
    for i in range (0,n):
        if x[i]<=X/2:
            leftvx2.append(vx[i]**2)
            leftvy2.append(vy[i]**2)
    temp=Tcal (np.average(leftvx2)+ np.average(leftvy2))
    return(left(x)* n*k*temp/X/Y*2)
    
def plenjon(x,y):  #lennard-johnes potential of a system
    e=0    
    for j in range (0,n):
        for i in range (0,n):
            for perx in [-1,0,1]:
                for pery in [-1,0,1]:
                    if perx!=0 or pery!=0 or i!=j:
                        dx= x[j]-x[i]+perx*X
                        dy= y[j]-y[i]+pery*Y
                        d= np.sqrt (dx**2+dy**2)
                        boo=sig/d
                        e+=4*ep*(boo**12-boo**6)
    return(e)
    
def auto_cor (vs,j):
    sigg= np.std(mean_v2**.5)
    boo=0
    for vv in range (0,len(vs)-j):
        boo+= np.average(vs[vv]*vs[vv+j])-np.average(vs[vv])*np.average(vs[vv+j])
    return boo/sigg**2
            
    
    
def lenjon (d): #lennard-johnes force between two
    boo=sig/d
    return (4*ep*(-12*boo**12/d+6*boo**6/d))
    
def lenajon (i): #lennard-johnes force accelerate on a particle
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
    
def left (x): #probablity of being on left side
    left=0
    for xx in x:
        if xx<=X/2:
            left+=1
    return (left/n)
T=.01 #time
h=.00001 #time error
n=100 #number of particles    
for T0 in [100]: #[10,20,50,100,150,200]:
    
    #fincor=np.zeros (int(T/h)-20)
    for koo in range (0,1):
        
        
        mean_v2=np.zeros(int(T/h))
        plenajon=np.zeros(int(T/h))
        
        Time=[] #time array for plotting
        
        
        m=6.6*10**-26 #mass of particles
        k=4*10**-4 #boltzman constant
        X=Y=16*10**8 #lengths of container
        ep=120*k#*10**44 lenard-johnes epsilon
        
        vmax=np.sqrt(3/4*k*T0/m) #calculated analytically
        sig=1 #potential sigma
        x=[] 
        y=[]
        lefts=[]  #probablity of being on the left side vs time
        vs=[] 
        for dx in np.arange(X/20,X/2+1,X/20): #arranging particles on the left side
            for dy in np.arange(Y/11,Y/11*10+1,Y/11):
                x.append(dx)
                y.append(dy)
        #x=np.random.rand (n)*X
        #y=np.random.rand (n)*Y
        vx=vmax*(.5-np.random.rand (n))*2
        vy=vmax*(.5-np.random.rand (n))*2
        ax=np.zeros (n)
        ay=np.zeros (n)
        Ps=[] #pressures
        Ts=[] #tempratures
        Es=[] #energies
        
        
        autocor=[]
        
        plen0=plenjon (x,y)
        
        for i in range (0,n): #calculating a0
            ax[i],ay[i]=lenajon(i)
        
        for t in range (1, int(T/h)+1):
            '''plt.figure()
            plt.ylim(0,Y)
            plt.xlim (0,X)
            plt.scatter(x, y)
            #print(np.sum(vx))
            #plt.scatter(x[0], y[0], c='red')
            #plt.scatter(x[1], y[1], c='blue')
            tim=(t-1)*h
            plt.title('t=%s'%tim)
            plt.savefig('%s'%(t-1))'''
            Time.append((t-1)*h)
            V2=vx**2+vy**2
            mean_v2[t-1]=avg(V2)
            plenajon[t-1]=plenjon(x, y)
            #print (mean_v2[t-1])
            lefts.append(left(x))
            Ts.append (T0-4*(plenajon[t-1]-plen0)/n/k) 
            Ps.append( P(x,vx,vy))
            Es.append(n*m/2*mean_v2[t-1]+plenajon[t-1])
            for i in range (0,n):
                fx=0
                fy=0
                x[i]=(x[i]+vx[i]*h+ax[i]*h**2/2)%X
                y[i]=(y[i]+vy[i]*h+ay[i]*h**2/2)%Y
                apx,apy=lenajon(i)
                vx[i]+=(apx+ax[i])/2*h
                vy[i]+=(apy+ay[i])/2*h
                ax[i]=apx
                ay[i]=apy
            '''
            if t>=20:
                autocor.append(auto_cor(vs,10))
                
        fincor=autocor
        '''
    
    #Es= n*m*mean_v2/2 - plenajon
    #Ts= Tcal(mean_v2)
    #Ps= P (Ts)
    
    
    plt.figure()
    plt.plot(Time, lefts)
    plt.title('left vs time')
    plt.xlabel('time')
    plt.ylabel('left')
    plt.savefig('left vs time h10-3')
    
    '''
    plt.figure()
    plt.plot(Time[19:int(T/h)], fincor[0:int(T/h)-2])
    plt.title('autocor vs time')
    plt.xlabel('time')
    plt.ylabel('autocor')
    plt.savefig('autocor vs time h10-3')
    ''''''
    for i in range (0,len (fincor)-1):
        if fincor [i+1]>.1:
        
            Tst.append((21+i)*h)
            TTs.append(T0)
            break
    

    '''
    plt.figure()
    plt.plot(Time, Ts)
    plt.title('T vs time h10-4 T0=%s'%T0)
    plt.xlabel('time')
    plt.ylabel('T')
    #plt.savefig('T vs time h10-4')
    
    plt.figure()
    plt.plot(Time, Ps)
    plt.title('P vs time')
    plt.xlabel('time')
    plt.ylabel('P')
    #plt.savefig('P vs time h10-3')
    
    pep=-plenajon*10**34+n*k*T0/4
    plt.figure()
    plt.plot(Time, pep)
    plt.title('E vs time')
    plt.xlabel('time')
    plt.ylabel('E')
    #plt.savefig('plenajon vs time h10-3')
    ''''''
    
'''
plt.figure()
plt.plot (TTs,Tst)
plt.title('stablity time vs T')
plt.show()
'''
print("--- %s seconds ---" % (time.time() - start_time)) #runtime
