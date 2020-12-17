# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:16:36 2019

@author: sushant
"""
import numpy as np

n_trials=1000

wins=0

for i in range(n_trials):

    car_door=np.random.randint(1,4)
    
    player_door1=np.random.randint(1,4)
    
    d=[1,2,3]
    
    d.remove(car_door)
    
    if player_door1 != car_door:
        
        d.remove(player_door1)
        
    host_door=np.random.choice(d)
        
        
    if (player_door1==car_door):
        
            wins = wins + 1
        
    p=(1*wins/n_trials)

wins2=0


for i in range(n_trials):
    
    car_door=np.random.randint(1,4)
    player_door2=np.random.randint(1,4)
    
    d=[1,2,3]
    
    d.remove(car_door)
    
    if (player_door2 != car_door):
        
        d.remove(player_door2)
        
    host_door2=np.random.choice(d)
                
    d=[1,2,3]

    d.remove(host_door2)
    d.remove(player_door2)
        
    player_door_changed=d[0]
        
    if (player_door_changed==car_door):
            
        wins2=wins2+1
            
    p2=(1*wins2/n_trials)
print('probability of winning when the door is changed:',p2)

print('probability of winning the car without changing doors:',p)     