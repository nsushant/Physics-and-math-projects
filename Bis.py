# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:26:54 2020

@author: sushant
"""

import numpy as np


alpha=float(input('Value to be square rooted:'))
x_low=0
x_high=max(alpha,1)
x_mid=x_high/2
x_change=x_high/4
root=np.sqrt(alpha)
count=0
f = open('root.csv','w')

while x_mid!=root:
    k=x_mid**2-alpha
    error=((abs(root-x_mid)/root)*100)
    a=x_mid
    b=error
    c=count
    if k>0:
        x_mid=x_mid-x_change
        count+=1
        error=((abs(root-x_mid)/root)*100)
        print(x_mid)
        f.write('{},{},{}\n'.format(a,b,c))
    if k<0:
        x_mid=x_mid+x_change
        count+=1
        error=((abs(root-x_mid)/root)*100)
        print(x_mid)
        f.write('{},{},{}\n'.format(a,b,c))
        
        
    x_change=x_change/2
    
    
f.close()

