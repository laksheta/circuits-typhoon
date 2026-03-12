# Numpy module is imported as 'np'
# Scipy module is imported as 'sp'
# The Schematic API is imported as 'mdl'
# To get the model file path, use 'mdl.get_model_file_path()'
# To print information to the console, use info()
import numpy as np

fsw = 10e3

T_plant = 1e-6
T_meas = 1e-6
T_wave  = 1e-6 
T_math  = 1e-6

V_in  = 780
V_out = 780
V1  = 780
V2  = 780
C   = 1e-6

n   = 1

P   = 10e3
D   = 0.5
L   = (V1*V2)*D*(1-D)/(2*fsw*P)

d   = 0.25
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
