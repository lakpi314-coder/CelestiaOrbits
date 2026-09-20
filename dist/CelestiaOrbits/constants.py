
#constants for this ig 
G =6.67e-11
M =5.9722e24
r =(6371e3)
scale =4.7e-7
pi_=3.141592653589
m = 1000 

#intial cordinents for primary and secondery bodies 
#velocities 
vx = 7800
vy = 0
vz = 0
vx_p = 0
vy_p = 0 
vz_p = 0

#postioning
x = 0
z = r +(100e3)
y  =0
x_earth = 0
y_earth = 0
z_earth = 0

#timing 
dt = 10
t  = 0
Orbit_Counter = 0
#parmeters for the moon 
y_moon =0
x_moon = 0
z_moon = 363300e3
vx_moon =1081.901
vy_moon = 0
vz_moon =0
radius_moon = 1737.4e3 
moon_m =7.34e22 
scale_moon =1e-10
print(y_moon)

#ursina values 
speed = 5
sens  = 150
max_dt =10000
min_dt =1