# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:52:26 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
from random import randint
import numpy as np
import statistics

T=4
n=2000
l=200
fin = np.zeros (l)
finfin = []
X=[]

for count in range (0,l):
    X.append(count)
    count+=1

'''t=0
while t<T:
    i=0
    while i<n:
        x= randint (0,l-1)
        fin [x]+=1
        i+=1
    finfin.append(fin)
    t+=1'''
i=0
while i<n:
    fin[randint(0,l-1)]+=1
    i+=1
fin1=fin
finfin.append(fin1)
print (fin)
plt.bar(X, fin, color='yellow')

j=0
while j<n:
    x= randint (0,l-1)
    fin [x]+=1
    j+=1
fin2=fin
finfin.append(fin2)
print (fin)
plt.bar(X, fin, color='teal')


i=0
while i<n:
    x= randint (0,l-1)
    fin [x]+=1
    i+=1
finfin.append(fin)
plt.bar(X, fin, color='blue')



i=0
while i<n:
    x= randint (0,l-1)
    fin [x]+=1
    i+=1
finfin.append(fin)
count = 0
plt.bar(X, fin, color='purple')





plt.show()