# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 13:01:34 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
import random
import numpy as np
import statistics
import math
import pandas as pd
import time
start__time = time.time()

for k in range(3,8):
    
    N=10**k
    st=0
    end=2
    fx_arr=[]
    real_integral=.882081 #from wolframalpha online
    
    start_time = time.time()
    def func (x):
        return (math.e**-(x**2))
    
    for n in range (0,N):
        x=random.uniform(st, end) #n/N*2
        fx_arr.append(func(x))
    
    simple_integral= np.average (fx_arr)*(end-st)
    simple_stat_error=statistics.stdev(fx_arr)/N**.5
    simple_real_error= abs(simple_integral-real_integral)
    simple_time=time.time() - start_time
    
    start_time = time.time()
    
    f_g_arr=[]
    g_integ=1-math.e**(-2)
    
    
    def g_rev (x):
        return (-np.log(x))
    
    def g (x):
        return (math.e**(-x))
        
    
    for n in range (0,N):
        x=g_rev(random.uniform(g(end), g(st))) 
        f_g_arr.append(func(x)/g(x))
    
    
    intel_integral= np.average (f_g_arr)*g_integ
    intel_stat_error=statistics.stdev(f_g_arr)/N**.5
    intel_real_error= abs(intel_integral-real_integral)
    intel_time=time.time() - start_time
    print('         N              result             stat_err             real_err              time ')
    print('intel  ',N,' ',intel_integral,' ' ,intel_stat_error,' ' ,intel_real_error,' ' ,intel_time )
    print('simple ',N,' ',simple_integral,' ' ,simple_stat_error,' ',simple_real_error,' ' ,simple_time )