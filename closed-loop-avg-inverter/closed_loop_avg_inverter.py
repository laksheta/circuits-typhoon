# Numpy module is imported as 'np'
# Scipy module is imported as 'sp'
# The Schematic API is imported as 'mdl'
# To get the model file path, use 'mdl.get_model_file_path()'
# To print information to the console, use info()
import numpy as np

if 'info' not in globals():
    info = print

T_meas = 1e-6
tau = 1e-3

V_dc = 780
upper_lim = +V_dc/2
lower_lim = -V_dc/2

V_g = 220 * np.sqrt(2)
V_rms = 220
u_grid_d  = 220*np.sqrt(2)
V_peak    = u_grid_d
u_grid_q  = 0
u_grid_amp    = np.sqrt(u_grid_d**2+u_grid_q**2)
u_grid_ph     = np.arctan2(u_grid_q, u_grid_d)

F = 50
phase = np.array([0,-120,120])

L = 1e-3
R = L / tau

i_d = 10
i_q = 0
omega   = 2*np.pi*F

u_d = u_grid_d + R*i_d - omega*L*i_q
u_q = u_grid_q + R*i_q + omega*L*i_d

U_inv_amp = np.sqrt(u_d**2+u_q**2)
U_inv_ph  = np.arctan2(u_q, u_d)

f_wb_i = 1e3
omega_c = 2*np.pi*f_wb_i

Kp_i    = omega_c*L
Ki_i    = omega_c*R

info(f"u_d: {u_d:.2f}")
info(f"u_q: {u_q:.2f}")
