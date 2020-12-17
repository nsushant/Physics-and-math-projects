# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:51:34 2020

@author: sushant
"""

#Newton Raphson 
import numpy as np 

alpha=float(input('Value to be square rooted'))
root=np.sqrt(alpha)
x_high=alpha
x_low=0
x_mid=x_high/2
count=0
f=open("root(2).csv","w")
while x_mid!=root:
    
    x=(x_mid)-(x_mid**2-alpha)/(2*x_mid)
    x_mid=x
    count+=1
    error=((x_mid-root)/root)*100
    a=x_mid
    b=error
    c=count
    f.write('{},{},{}\n'.format(a,b,c))
    print(x_mid)
    print(error)
    print(count)
    
f.close()
