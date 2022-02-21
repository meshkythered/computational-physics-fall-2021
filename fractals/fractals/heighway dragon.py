# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:03:16 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
'''
          1,1



0,0                 2,0
'''
def fx1  (Arx,Ary): #left one for x
    Arx1=Arx/2- Ary/2
    return (Arx1)
    
def fy1  (Arx, Ary): #left one for y
    Ary1=Arx/2+ Ary/2 #one /2**.5 is for 45 deg and the other is for changing the length
    return (Ary1)

def fx2  (Arx,Ary): #right one for x
    Arx2=np.flip(-Arx/2- Ary/2)+2
    return (Arx2)
    
def fy2  (Arx, Ary): #right one for y
    Ary2=np.flip(+Arx/2- Ary/2)
    return (Ary2)

def ffx (Arx,Ary): #main f for x
    MX =np.append(fx1 (Arx ,Ary),fx2 (Arx ,Ary))
    return (MX)

def ffy (Arx,Ary): #main f for y
    MY =np.append(fy1 (Arx ,Ary),fy2 (Arx ,Ary))
    return (MY)


M1x= np.array ([0,2])# first coordinations
M1y= np.array ([0,0])


i=1
while i <14 :
    Mx=ffx (M1x ,M1y)
    My=ffy (M1x ,M1y)
    M1x=Mx
    M1y=My
    i+=1
    plt.figure()
    plt.title('heighway dragon %s stage'%i)
    plt.plot (M1x, M1y)
    plt.savefig('heighway dragon %s stage'%i)



    
    