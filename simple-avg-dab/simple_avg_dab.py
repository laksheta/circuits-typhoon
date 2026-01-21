# Numpy module is imported as 'np'
# Scipy module is imported as 'sp'
# The Schematic API is imported as 'mdl'
# To get the model file path, use 'mdl.get_model_file_path()'
# To print information to the console, use info()
import numpy as np

fsw = 10e3

T_meas = 10e-6
T_wave  = 1e-6
T_math  = 10e-6

V1  = 780
V2  = 780
C   = 1e-6

P   = 10e3
D   = 0.5
L   = (V1*V2)*D*(1-D)/(2*fsw*P)

d   = 0.5
deg = d*(90/0.5)
phi = (deg/360)*(1/fsw)

phi_pu = 1-phi*fsw

I = V1*D*(1-D)/(2*fsw*L)
R_load = V1/I