# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 01:41:47 2020

@author: sushant
"""
import numpy as np
import matplotlib.pyplot as plt

#initial conditions

delta_t= 10.0**-5.0
yi=-0.005
xi=np.arange(0,0.001,0.0001).tolist()
c=137.035999
vy=0.07*c
vx=0.0
v=0.0
a=0.0
ax=0.0
Vx=0.0

rx=[]
ry=[]

Rx=[]
Ry=[]

t=0.0

#choosing one of the initial values of x

for i in xi:
#Statement of initial conditions in the loop 
    x=i
    y=yi
    vy=0.07*c
    vx=0.0
    c=137.035999
    acy=0
    acx=0
    delta_t= 10.0**-5.0
    v=0.0
    Vx=0.0
    
#Looping over time steps upto the limit (infinite loop breaking at the limit) 
    
    while (True):
    
        acy=0.021*(y/(x**2.0+y**2.0)**1.5)
        acx=0.021*(x/(x**2.0+y**2.0)**1.5)
        
        v=vy+acy*delta_t
        Vx=vx+acx*delta_t
        
        ynew=y+vy*delta_t
        xnew=x+vx*delta_t
        
        rx.append(xnew)
        ry.append(ynew)
        
    #reseting values after operations    
        
        acy=0
        acx=0
        vy=v
        y=ynew
        vx=Vx
        x=xnew
        
        #Breaking the loop when the limit is reached
        
        if (1.1*np.sqrt(i**2+yi**2) < np.sqrt(x**2.0+y**2.0)):
            Rx.append(rx)
            Ry.append(ry)
            
            rx=[]
            ry=[]
            
            break 
       
#The above creates a list of lists (a list for each initial x value)

pos=[]
counter=0

#List of indicies of the list of lists

for i in Rx:
    counter+=1
    pos.append(counter-1)
        
#The following allows the lists of the same appendicies to be plotted together

for l in pos:
    
    plt.plot(Rx[l],Ry[l])
    plt.xlabel('X-position of the particle')
    plt.ylabel('Y-position of the particle')
    
 
#Plotting the output 
    
px= plt.gca()
px.set_aspect('equal')

#Marking the position of the gold nucleus 

plt.scatter([0.0],[0.0]) 
plt.show()

        


        
    