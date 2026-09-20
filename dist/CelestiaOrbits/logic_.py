import math


def angle_ref_isolated():
    import constants as const 
    
    theta = math.radians(5.145)
    
    # Calculate height
    z = math.tan(theta) * 363300e3
    return z
def Time_precent(t,x,y,z):
    global orbit_counter
    import constants as const 
    T_moon =math.sqrt(4*math.pi*(384399e3)**3/(const .G*(const .M+const .moon_m))) 
    T_sat  =math.sqrt(4*math.pi*(math.hypot(x,y,z))**3/(const .G*(const .M)))
    Time  =(t/T_sat)*100
    return Time 
def velocity_cal_sat(vx,vy,vz):
    velocity_sat =math.hypot(vx,vy,vz)
    return velocity_sat


def EscapeVelocity(x,y,z):
    import constants as const 
    r =math.hypot(x,y,z)
    v =math.sqrt(2*const.G*const.M/r)
    return v 