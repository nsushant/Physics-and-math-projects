"""
created 28.12.2021 by sushanta nigudkar

(from osteile)These units make it possible for gravitational constant to equal 1 (G=1).
    
1 unit of Mass     = 2x10^(10) Solar Masses
1 unit of Distance = 500 pc
1 unit of Time     = 1.2 million years
1 unit of Velocity = 400 km/s

"""

import numpy as np 
import matplotlib.pyplot as plt 

# simulations params
softening = 2.0
G   = 1
dims_space = 3

# number of rings 
n_rings = 10
# diameter of each ring (https://www.messier-objects.com/messier-51-whirlpool-galaxy/)
# rounded to 2 s.f.
d  = 52.0
# radius of each ring
r  = d / 2.0

# generate rings of stars 

# get the radii of the individual rings 
r_individual = np.arange(0, r +(r/n_rings), r/n_rings)

# divide each ring into parts = no. of pacrticles  
rad_stars = np.linspace(0,2*np.pi,50)

# initial position of spiral galaxy  
spiral_pos_init = [0.0,0.0,0.0]
# initial velocity
initial_gal_v = [0,0,0.0]
# initial position of companion (from ostile)
companion_pos_init = [-30.0,-30.0,0]
# initial velocity
initial_companion_v = [0,0.34,0.34]
# galaxy masses 
spiral_mass      = 5.0
companion_mass = (0.25) * spiral_mass


# time constraints
h        = 1.0
h_half   = 0.5 * h
sqr_h_half= 0.5 * h**2
# from Ostile
timesteps = 540 
time      = np.arange(0,timesteps+1,h)


# define acceleration functions 

#compute acceleration of stars 

def stars_acc(pos_gal,pos_stars,pos_companion,ma,mb,G,s):

    acceleration_stars = [[],[],[]]
    
    if len(pos_stars.shape)>1:
        diff = [pos_gal[i]- pos_stars[:,i] for i in range(3)]
        diffb =[pos_companion[i]- pos_stars[:,i] for i in range(3)]
    if len(pos_stars.shape)==1:
        diff = [pos_gal[i]- pos_stars[i] for i in range(3)]
        diffb =[pos_companion[i]- pos_stars[i] for i in range(3)]
        
    ra = np.sqrt(diff[0]**2 + diff[1]**2 + diff[2]**2 + s**2)
    rb = np.sqrt(diffb[0]**2 + diffb[1]**2 + diffb[2]**2  + s**2)
    #r = np.sqrt(xstars**2 + ystars**2+ zstars**2)
    
    acceleration_stars[0]= ((G*ma*(diff[0])/((ra)**(3))) + (G*mb*(diffb[0])/((rb)**(3))))
    acceleration_stars[1]= ((G*ma*(diff[1])/((ra)**(3))) + (G*mb*(diffb[1])/((rb)**(3))))
    acceleration_stars[2]= ((G*ma*(diff[2])/((ra)**(3))) + (G*mb*(diffb[2])/((rb)**(3))))
   
    return np.array(acceleration_stars),ra,rb

#compute acceleration of spiral galaxy 
def gal_acc(pos_gal, pos_companion,mcompanion,G,s):
    
    acceleration_gal = [[],[],[]]
    
    diff_gal = np.array(pos_companion) - np.array(pos_gal)
    
    r_gal =np.sqrt((diff_gal[0])**2 + (diff_gal[1])**2 + (diff_gal[2])**2 + s**2)    
    
    acceleration_gal[0]= (G*mcompanion*(diff_gal[0])/((r_gal)**(3))) 
    acceleration_gal[1]= (G*mcompanion*(diff_gal[1])/((r_gal)**(3))) 
    acceleration_gal[2]= (G*mcompanion*(diff_gal[2])/((r_gal)**(3))) 
   
    
    return np.array(acceleration_gal),r_gal


#compute acceleration of companion
def comp_acc(pos_gal, pos_companion,mgal,G,s):
    
    acceleration_companion = [[],[],[]]
    
    diff_companion = np.array(pos_gal) - np.array(pos_companion)
    
    r_companion = np.sqrt((diff_companion[0])**2 + (diff_companion[1])**2 +
    (diff_companion[2])**2 + s**2)   
    
    acceleration_companion[0]= (G*mgal*(diff_companion[0])/((r_companion)**(3))) 
    acceleration_companion[1]= (G*mgal*(diff_companion[1])/((r_companion)**(3))) 
    acceleration_companion[2]= (G*mgal*(diff_companion[2])/((r_companion)**(3))) 
   
    
    return np.array(acceleration_companion),r_companion



x_stars = []
y_stars = []

# making x,y pos arrays 
for p in range(len(r_individual)):
    for i in range(len(rad_stars)):
        x_stars.append(r_individual[p]*np.cos(rad_stars[i]))   
        y_stars.append(r_individual[p]*np.sin(rad_stars[i])) 


# generate initial conditions      
# the total number of stars
total_stars = len(y_stars)
# initial star arrays 

star_pos = np.zeros([timesteps,total_stars,dims_space])

star_vel = np.zeros([timesteps,total_stars,dims_space])

star_acc = np.zeros([timesteps,total_stars,dims_space])


# creating an initial pos-array for the stars 
star_pos[0][:,0] = x_stars
star_pos[0][:,1] = y_stars
star_pos[0][:,2] = np.zeros(total_stars)

# creating initial pos arrays for the spiral galaxy and the companion 
spiral_pos = np.zeros([timesteps,dims_space])
companion_pos = np.zeros([timesteps,dims_space])

spiral_v  = np.zeros([timesteps,dims_space])
companion_v  = np.zeros([timesteps,dims_space])

spiral_acc = np.zeros([timesteps,dims_space])
companion_acc = np.zeros([timesteps,dims_space])

spiral_pos[0]  = spiral_pos_init[0], spiral_pos_init[1], spiral_pos_init[2]
spiral_v[0]   = initial_gal_v[0], initial_gal_v[1], initial_gal_v[2]

companion_pos[0]  = companion_pos_init[0],companion_pos_init[1], companion_pos_init[2]
companion_v[0]   = initial_companion_v[0], initial_companion_v[1], initial_companion_v[2]


# calculate the accelerations of the stars 
for i in range(len(star_pos)):
    
    stars_accel_calc, r1, r2 = stars_acc(spiral_pos[0], 
    star_pos[i],companion_pos[0],spiral_mass,companion_mass, G,softening)

    star_acc[i][:,0] = stars_accel_calc[0]  
    star_acc[i][:,1] = stars_accel_calc[1] 
    star_acc[i][:,2] = stars_accel_calc[2]  
    break


# velocity verlet integration
for t in range(1,timesteps):
    
    # get estimated positions 
    spiral_pos[t] = spiral_pos[t-1] + spiral_v[t-1]*h + sqr_h_half * spiral_acc[t-1]\
    companion_pos[t] = companion_pos[t-1] + companion_v[t-1]*h + sqr_h_half * companion_acc[t-1]
        
    # compute accelerations
    a_comp, s = comp_acc(spiral_pos[t], companion_pos[t], spiral_mass, G,softening)
    a_gal, sr = gal_acc(spiral_pos[t], companion_pos[t],companion_mass, G,softening)

    # get estimated velocities
    spiral_v[t] = spiral_v[t-1] + h_half * (a_gal + spiral_acc[t-1])
    companion_v[t] = companion_v[t-1] + h_half * (a_comp + companion_acc[t-1])
        
    spiral_acc[t] = a_gal
    companion_acc[t] = a_comp

# once time integration for the central masses has been performed, 
# perform time integration for the massless stars 

for t in range(1,timesteps):
    for s in range(total_stars):
        # estimate stellar positions 
        star_pos[t][s][0] = star_pos[t-1][s][0] + star_vel[t-1][s][0]*h +\ 
                                        sqr_h_half * star_acc[t-1][s][0]
        star_pos[t][s][1] = star_pos[t-1][s][1] + star_vel[t-1][s][1]*h +\ 
                                        sqr_h_half * star_acc[t-1][s][1]
        star_pos[t][s][2]= star_pos[t-1][s][2] + star_vel[t-1][s][2]*h +\ 
                                        sqr_h_half * star_acc[t-1][s][2]

        # get stellar accelerations
        star_cords = star_pos[t][s][0], star_pos[t][s][1],star_pos[t][s][2]
        stars_accel_calc, r1, r2 = stars_acc(spiral_pos[t],star_pos[t][s],companion_pos[t],\
        spiral_mass,companion_mass, G,softening)

        # estimate stellar velocities
        star_vel[t][s][0] = star_vel[t-1][s][0] + h_half * (stars_accel_calc[0] +\  
        star_acc[t-1][s][0])
        star_vel[t][s][1] = star_vel[t-1][s][1] + h_half * (stars_accel_calc[1] +\  
        star_acc[t-1][s][1])
        star_vel[t][s][2] = star_vel[t-1][s][2] + h_half * (stars_accel_calc[2] +\  
        star_acc[t-1][s][2])
    
        # assign the computed acceleration to the acceleration array
        star_acc[t][s][0] = stars_accel_calc[0]
        star_acc[t][s][1] = stars_accel_calc[1]
        star_acc[t][s][2] = stars_accel_calc[2]

     
       
# color particles by their initial distance from the center
pos_0 = np.sqrt((spiral_pos[0][0]-star_pos[0][:,0])**2 +\ 
(spiral_pos[0][1]-star_pos[0][:,1])**2 + (spiral_pos[0][2]-star_pos[0][:,2])**2)

# the timestep to be plotted 
view_time =150

# plot the positions of the stars with colouring based on their positions in the first snapshot
plt.scatter(star_pos[view_time][:,0],star_pos[view_time][:,1],marker='*', label = 'Stars',c=pos_0)
# plot the rest of the components 
plt.scatter(companion_pos[view_time][0],companion_pos[view_time][1],marker='o',\  
label='Companion', c='r', s=220)
plt.scatter(spiral_pos[view_time][0],spiral_pos[view_time][1],marker='+', label = 'Spiral\ 
Center',c='k', s=200)
plt.ylabel('y')
plt.xlabel('x')
cbar = plt.colorbar()
cbar.ax.set_yticklabels([ '0',  '5', '10', '15', '20', '25'])
cbar.set_label('Initial distance from center')
