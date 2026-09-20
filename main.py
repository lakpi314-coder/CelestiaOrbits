import sys 
import math
from ursina import *
import constants as const
import logic_ as l 

if sys.platform == "darwin":
    from panda3d.core import loadPrcFileData
    loadPrcFileData('', 'gl-version 3 3')
    loadPrcFileData('', 'notify-level-glgsg fatal')






#the app configuration 
app =Ursina()
mouse.locked =True
#the earth is the earth and sec is the secondery body
camera.position =(10,10,0)
camera.rotation=Vec3(45,271,0)

earth=Entity(model="sphere",scale=const.r*const.scale,color=color.blue,collider="sphere") 
Entity(model='cube', scale=(1000, 1, 1000), color=color.gray, y=-500)
sec  =Entity(model="sphere",color=color.red,scale= 0.2,collider="sphere")#the scaling used for this is not realistic
moon =Entity(model="sphere",scale =const.radius_moon*const.scale+1,color=color.white)
#text on the screem
Velocity_sat =Text(text="",color=color.white,position=(-0.85,0.45))
Time_text =Text(text="",color =color.white,position=(-0.85,0.40))
const.y_moon = (l.angle_ref_isolated()) #seting the inclination for the moon 
def update():
    
    dx = const.x-const.x_earth
    dy = const.y-const.y_earth
    dz = const.z-const.z_earth

    forcex=-const.G*const.M*const.m*dx/math.hypot(dx,dy,dz)**3
    forcey=-const.G*const.M*const.m*dy/math.hypot(dx,dy,dz)**3
    forcez=-const.G*const.M*const.m*dz/math.hypot(dx,dy,dz)**3
    #force that the sat exercts upon the moon 
    dx_moon =const.x_moon - const.x 
    dy_moon =const.y_moon - const.y
    dz_moon =const.z_moon - const.z
     

    forcex_moon =const.G*const.moon_m*const.m*dx_moon/math.hypot(dx_moon,dy_moon,dz_moon)**3    
    forcey_moon =const.G*const.moon_m*const.m*dy_moon/math.hypot(dx_moon,dy_moon,dz_moon)**3
    forcez_moon =const.G*const.moon_m*const.m*dz_moon/math.hypot(dx_moon,dy_moon,dz_moon)**3
    
    force_moon_x= -forcex_moon
    force_moon_y= -forcey_moon
    force_moon_z= -forcez_moon

    const.vx +=(forcex/const.m)*const.dt +((force_moon_x/const.m)*const.dt)
    const.vy +=(forcey/const.m)*const.dt+((force_moon_y/const.m)*const.dt)
    const.vz +=(forcez/const.m)*const.dt+((force_moon_z/const.m)*const.dt)

    const.x +=const.vx*const.dt
    const.y +=const.vy*const.dt
    const.z +=const.vz*const.dt

    #gravity felt by the earth and therefore the postioning updating for the earth 
    forcex_earth = -forcex
    forcey_earth = -forcey
    forcez_earth = -forcez
    

    #gravity moon 
    dx_earth_moon =const.x_moon -const.x_earth
    dy_earth_moon =const.y_moon -const.y_earth
    dz_earth_moon =const.z_moon -const.z_earth

    forcex_earth_moon =-const.G*const.M*const.moon_m*dx_earth_moon/math.hypot(dx_earth_moon,dy_earth_moon,dz_earth_moon)**3
    forcey_earth_moon =-const.G*const.M*const.moon_m*dy_earth_moon/math.hypot(dx_earth_moon,dy_earth_moon,dz_earth_moon)**3
    forcez_earth_moon =-const.G*const.M*const.moon_m*dz_earth_moon/math.hypot(dx_earth_moon,dy_earth_moon,dz_earth_moon)**3
    

    
    #updating the moons postion and velocity 
    const.vx_moon +=(forcex_earth_moon/const.moon_m)*const.dt+((forcex_moon/const.moon_m)*const.dt)
    const.vy_moon +=(forcey_earth_moon/const.moon_m)*const.dt+((forcey_moon/const.moon_m)*const.dt)
    const.vz_moon +=(forcez_earth_moon/const.moon_m)*const.dt+((forcez_moon/const.moon_m)*const.dt) 

    const.x_moon += const.vx_moon*const.dt 
    const.y_moon += const.vy_moon*const.dt 
    const.z_moon += const.vz_moon*const.dt 
    
    #gravity felt from the moon to the earth

    forcex_moon_earth = -forcex_earth_moon
    forcey_moon_earth = -forcey_earth_moon
    forcez_moon_earth = -forcez_earth_moon

    const.vx_p +=(forcex_earth/const.M)*const.dt +((forcex_moon_earth/const.M)*const.dt)
    const.vy_p +=(forcey_earth/const.M)*const.dt +((forcey_moon_earth/const.M)*const.dt)
    const.vz_p +=(forcez_earth/const.M)*const.dt +((forcez_moon_earth/const.M)*const.dt) 

    const.x_earth +=const.vx_p*const.dt 
    const.y_earth +=const.vy_p*const.dt
    const.z_earth +=const.vz_p*const.dt
   
   #updating the positions for the objects 
    sec.x = const.x*const.scale
    sec.y = const.y*const.scale
    sec.z = const.z*const.scale
    earth.x = const.x_earth*const.scale 
    earth.y = const.y_earth*const.scale 
    earth.z = const.z_earth*const.scale
    moon.x = const.x_moon*const.scale
    moon.y = const.y_moon*const.scale
    moon.z = const.z_moon*const.scale
    print(f"velocity:{const.vx_moon},postion:{const.z_moon}")
    #updating time vaules 
    #and running text to ursina(ik shit kinda old )
    const.t +=const.dt #recording time elapsed  ig 
    Orbit_Precentage=l.Time_precent(const.t,const.x,const.y,const.z)
    
    v_sat =l.velocity_cal_sat(const.vx,const.vy,const.vz)
    Velocity_sat.text =f"Veloctiy of the sat: {v_sat} m/s"
    
    if Orbit_Precentage >100:
        const.t =0 
        const.Orbit_Counter +=1
    
    Time_text.text =f"Orbit counter:{const.Orbit_Counter}"
    
    EscapeEarth =l.EscapeVelocity(const.x,const.y,const.z)
    #keybindings 
    if held_keys['w']:
        camera.position +=camera.forward*const.speed*time.dt
    
    if held_keys['s']:
        camera.position -=camera.forward*const.speed*time.dt 
    
    if held_keys['a']:
         camera.position +=camera.left*const.speed*time.dt
    
    if held_keys['d']:
        camera.position -=camera.left*const.speed*time.dt
    
    if held_keys['t']:
        const.dt +=1
        
        if const.dt >const.max_dt:
            const.dt = const.max_dt
    
    if held_keys['g']:
        const.dt -=1
        
        if const.dt <const.min_dt:
            const.dt =const.min_dt
    
    if held_keys['i']:#velocity increasing 
        const.vx +=100
        if v_sat>EscapeEarth:
           Velocity_sat.color=color.red 
        if v_sat <EscapeEarth:
            Velocity_sat.color=color.white 

    if held_keys['k']:
        const.vx  -=100 
    
    if held_keys['r']:
        const.x =0
        const.y =0
        const.z =const.r+(100e3)
        const.vx=7844.04
        const.vy =0
        const.vz =0
    
    if held_keys['e']:
        mouse.locked = False
        const.dt = 0
    if held_keys['`']:
        mouse.locked =True 
        const.dt =1
    #mouse 
    camera.rotation_y += mouse.velocity[0] * const.sens
    camera.rotation_x -= mouse.velocity[1] * const.sens 

app.run()