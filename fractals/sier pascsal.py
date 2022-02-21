# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:43:17 2021

@author: ASUS
"""
'''
           (0,0)
           
     (-1,-1)   (1,-1) 
             .
             .
             .
'''

from math import factorial #factoriel technique used instead of summing
import numpy as np
import matplotlib.pyplot as plt

Arx =[] #x coordinations
Ary =[] #y coord
Arva =[] #values

count=0 
i=0 #counts rows
j=0 #counts columns (i know they arent exactly columns :)) 

n=1024 #how many rows
while i<=n:
    while j<=i:
        
        # value = n!/((n-r)!*r!)
        Arva.append(factorial(i)//(factorial(j)*factorial(i-j)))
        Ary.append( -1*i)
        Arx.append(-1*i +2*j)
        count+=1
        j+=1
    i+=1
    j=0
    


i=0
final_x = []
final_y = []
for i in range( count-1 ):
    if (Arva [i] % 2) == 1:
        final_x.append (Arx[i])
        final_y.append (Ary[i])
        plt.figure()
        plt.title('pascal sierpinsky %s dots'%i)
        plt.scatter(final_x, final_y, 3000*32/n**2*50)
        plt.savefig('pascal sierpinsky %s dots'%i)
    i+=1
        
    
        
plt.scatter(final_x, final_y, 3000*32/n**2)
  
plt.show()   