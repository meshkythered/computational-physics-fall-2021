# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:45:40 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
import numpy as np
from random import randint
import math 


k=50
Li=1000
Lr=1000
ArR = [] 
ArI = [] 
fin= np.zeros ((2*Lr,2*Li)) #matrix of the times the f^n(z) stayed finite when cell number is real and imaginary part of dots 
R0=0.7885* math.sin(math.pi*k/25) #copied from wikipedia :))))
I0=0.7885* math.cos(math.pi*k/25)
def f (R, I): #julia function
    R2= R**2-I**2 +R0
    I2= 2*I*R + I0
    return (R2, I2)


for i0 in range (-1000, 1001): #checking for all coordinations in space
    for r0 in range (-1000, 1001):
        r=r0/400 #here's for the resolution
        i=i0/400
        count =0
        while (count<25):
            r,i= f (r,i)
            if (abs (complex(r,i))>10):
                break
            count+=1
        fin [r0+999][i0+999]=count/25 #count is the number of times f^n(z) stayed in the said range


plt.imshow(fin, cmap='twilight_shifted') #to show with shades
plt.axis('off')
plt.show()



    