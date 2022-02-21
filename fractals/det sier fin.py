# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:07:51 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from random import randint
  
'''            (0,0)=1



(-1,-1)=2                (1,-1)=3
'''

def newtr (dot1,dot2,dot3): #ایکس یا ایگرگ سه راس را میگیره تبدیل به سه دسته راس سه تایی میکنه
    dot4=(dot1+dot2)/2
    dot5=(dot3+dot2)/2
    dot6=(dot1+dot3)/2
    return (dot1,dot4,dot6,dot2,dot5,dot4, dot3,dot5,dot6)

def ff (arr): #تابع نهایی که یک بار روی ایگرگ ها و یک بار روی ایکس ها اعمال میشود
    X=[]
    i=0
    for i in range (0,num):
        X.extend(newtr(arr[3*i], arr[3*i+1], arr[3*i+2]))
        print ('boom')
    return (X)


Arx =[0,-1,1] #مجموعه ایکس ها به ترتیب، اینها تک به تک جفت ایگرگ ها هستند و سه تا سه تا یک مثلث را نشان میدهند
Ary= [0,-1,-1]
num =1 #تعداد کل مثلث ها که یک سوم طول ارری هاست

i=0
while i<10: #تعداد مراحل
    Arx= ff(Arx)
    Ary= ff(Ary)
    num*=3
    i+=1
    plt.figure()
    j=0
    while j<num: #نشان دادن
        plt.fill(Arx[j*3:j*3+3],Ary[j*3:j*3+3])
        j+=1
    plt.title('det sirepinsky stage %s'%i)
    plt.savefig('det sirepinsky stage %s'%i)
'''    
i=0
while i<num: #نشان دادن
    plt.fill(Arx[i*3:i*3+3],Ary[i*3:i*3+3])
    i+=1
plt.show()
'''