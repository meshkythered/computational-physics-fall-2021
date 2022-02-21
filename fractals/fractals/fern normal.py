# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 20:20:32 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
from random import randint
  

Arx = []
Ary = []
  

Arx.append(0) #first
Ary.append(0) #first
  
count = 0
  
for i in range(1, 30000):
  
    z = randint(1, 100) 
      

    if z < 4:
        Arx.append(0)
        Ary.append(0.25*(Ary[count])-.4)
      
    if z>= 2 and z<= 86:
        Arx.append(0.95*(Arx[count]) + 0.005*(Ary[count])-.002)
        Ary.append(-0.005*(Arx[count]) + 0.93*(Ary[count])+.5)
      
  
    if z>= 87 and z<= 93:
        Arx.append(0.035*(Arx[count]) - 0.2*(Ary[count])-.09)
        Ary.append(0.16*(Arx[count]) + 0.04*(Ary[count])+.02)
      
 
    if z>= 94 and z<= 100:
        Arx.append(-0.04*(Arx[count]) + 0.2*(Ary[count])+.1)
        Ary.append(0.15*(Arx[count]) + 0.04*(Ary[count])+.07)
          
    count += 1
   
plt.scatter(Arx, Ary, 0.1, edgecolor ='green')
  
plt.show()   