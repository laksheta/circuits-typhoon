import numpy as np

fsw = 10e3
T = 1/fsw

T_meas = 2e-6
T_wave  = 2e-6  
T_math  = 1e-6
T_delay = 2e-6
T_plant = 0.1e-6

delay_deg   = 45
delay_N = ((delay_deg/360)*T)/T_delay

V_in  = 780
V_out = 780
V1  = 780
V2  = 780
C   = 1000e-6

P   = 10e3
D   = 0.5
L   = (V1*V2)*D*(1-D)/(2*fsw*P)

d   = 0.5
deg = d*(90/0.5)
phi = (deg/360)*(1/fsw)

phi_pu = 1-phi*fsw

I = V1*D*(1-D)/(2*fsw*L)
R_load = V1/I

P_c = 5e3
R_load_c  = (V_out**2) / P_c 

d_c = d*0.5

Gdc     = ((R_load_c)/(2*V_out))*((V1*V2*(1-2*d_c)/(2*fsw*L)))
tau     = (C*R_load_c)/2

f_bw    = 0.05*fsw
omega_c = 2*np.pi*f_bw

K_p      = (tau*omega_c)/Gdc
K_i      = K_p/tau
