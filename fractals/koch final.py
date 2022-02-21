# -*- coding: utf-8 -*-

"""
Created on Mon Sep 20 14:38:31 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt


len = 1 #physical length


def f2x (ArX ,ArY): #2nd on left with 60 rotatation and (1.5 len, sqrt3/2 len) shift
    ArX2= ArX/2- ArY*3**0.5/2 +len
    return ArX2

def f2y (ArX ,ArY): #2nd on left for y
    ArY2= ArX*3**(0.5)/2+ ArY/2
    return ArY2

#########


def f3x (ArX ,ArY): #3rd on left with -60 rotatation and (1.5 len, sqrt3/2 len) shift
    ArX3=(ArX/2+ArY*3**(0.5)/2)+len*1.5
    return ArX3

def f3y (ArX ,ArY): #3rd on left for y
    ArY=(ArY/2-ArX*3**(0.5)/2)+len*3**0.5/2
    return ArY
    
##########


def f4x (ArX): #4th on left for x (y remains unchanged)
    ArX4= ArX+2*len
    return (ArX4)


########

def Fx (ArX ,ArY): #main f for x
    MX =np.append(ArX,[f2x (ArX ,ArY),f3x (ArX ,ArY),f4x (ArX)])
    return (MX)

def Fy (ArX ,ArY): #main f for y
    #print (ArY )
    MY =np.append (ArY, [f2y (ArX ,ArY),f3y (ArX ,ArY), ArY])
    return (MY)


M1X= np.array ([0,1])
M1Y= np.array ([0,0])


M2X = Fx (M1X, M1Y)
M2Y = Fy (M1X, M1Y)
'''len =len *3

M3X = Fx (M2X, M2Y)
M3Y = Fy (M2X, M2Y)
len =len *3'''


'''plt.plot (M3X, M3Y)
plt.show ()'''

def FF (ArX ,ArY):
    MY=Fy (ArX ,ArY)
    MX=Fx (ArX ,ArY)
    return (MX, MY)

n=6
i=1
while i <9 : #the number of levels
    MY=Fy (M1X ,M1Y)
    MX=Fx (M1X ,M1Y)
    M1X=MX
    M1Y=MY
    len*=3
    i+=1
    plt.figure()
    plt.ylim(0,3**(i-2)*2.5)
    plt.title('koch %s stage'%i)
    plt.plot (M1X, M1Y)
    plt.savefig('koch %s stage'%i)


    
    
        
