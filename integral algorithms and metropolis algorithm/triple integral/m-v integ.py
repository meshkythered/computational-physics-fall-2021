# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:24:05 2021

@author: ASUS
"""

import matplotlib.pyplot as plt
import random
import numpy as np
import statistics
import math
import pandas as pd
import time
start_time = time.time()

rho0=5 #aint important
r=10
N=1200 
# 3 functions for three dimentions: integx, integy, integz , density varies in z direction, o=(0,0,r)

def integx (z,y):
    stx=-(r**2-(z-r)**2-y**2)**.5
    endx=(r**2-(z-r)**2-y**2)**.5
    mox=[] #x dm
    mx=[] #dm
    rhox=rho0*(1+z/(2*r))
    for nx in range (0,N):
        x=random.uniform(stx, endx)
        mox.append(rhox*x)
        mx.append(rhox)
    mcmx=np.average(mox)*(endx-stx)
    dmx=np.average(mx)*(endx-stx)
    return(mcmx,dmx)

def integy (z):
    sty=-(r**2-(z-r)**2)**.5
    endy=(r**2-(z-r)**2)**.5
    moy_ar=[] #y dm
    my_ar=[] #dm
    cmx_y_ar=[] #xcm until y calculation
    
    for ny in range (0,N):
        y=random.uniform(sty, endy)
        mcmx,mx=integx(z,y)
        moy_ar.append(mx*y)
        my_ar.append(mx)
        cmx_y_ar.append(mcmx)
    
    moy=np.average(moy_ar)*(endy-sty)
    my=np.average(my_ar)*(endy-sty)
    cmx_y=np.average(cmx_y_ar)*(endy-sty)
    return(moy,my,cmx_y)

def integz () :
    stz=0
    endz=2*r
    moz_ar=[] #z.dm
    mz_ar=[] #dm until z integral
    xcm_z_ar=[] #x.dm until z
    ycm_z_ar=[] #y.dm until z
    
    for nz in range (0,N):
        z=random.uniform(stz, endz)
        ycm,my,xcm=integy(z)
        moz_ar.append(my*z)
        mz_ar.append(my)
        xcm_z_ar.append(xcm)
        ycm_z_ar.append(ycm)
    
    moz=np.average(moz_ar)*(endz-stz)
    mz=np.average(mz_ar)*(endz-stz)
    xcm_z=np.average(xcm_z_ar)*(endz-stz)
    ycm_z=np.average(ycm_z_ar)*(endz-stz)
    
    return(moz/mz,xcm_z/mz,ycm_z/mz)

zcm,xcm,ycm=integz()
zcm-=r
zre= abs(zcm-r/15) #z real error
xre= abs(xcm)
yre= abs(ycm)

print("--- %s seconds ---" % (time.time() - start_time)) #runtime