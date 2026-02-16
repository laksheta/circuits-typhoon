import numpy as np


exec_meas   = 1e-6
exec_sine   = 1e-6
exec_controller = 1e-6

V_grid_peak = 220*np.sqrt(2)
V_grid_rms  = 220
F           = 50
omega       = 2*np.pi*F

f_sw        = 50e3

R           = 1e-1
L           = 1e-3

R_load      = 100
C_out       = 10e-6

V_dc_target = 800

P_load = (V_dc_target**2) / R_load

i_d_req = -(2 * P_load) / (3 * V_grid_peak)
i_q_req = 0

u_d = V_grid_peak - (R * i_d_req - omega * L * i_q_req)
u_q = 0 - (R * i_q_req + omega * L * i_d_req)

U_rect_amp = np.sqrt(u_d**2 + u_q**2)
U_rect_rms = U_rect_amp/np.sqrt(2)
delta_rad  = np.arctan2(u_q, u_d)
delta      = delta_rad * (180/np.pi)

m = U_rect_amp / V_dc_target

phase = [0+delta, -120+delta, 120+delta]
phase_3ph    = delta

V_rect = m*V_dc_target

# Controller
f_bw_i      = f_sw*0.1
omega_ci    = 2*np.pi*f_bw_i
Kp_i        = 0.1* omega_ci * L
Ki_i        = 0.1* omega_ci * R

f_bw_v      = 20
omega_cv    = 2*np.pi*f_bw_v
zeta        = 0.707
Kp_v        = 0.1*2*zeta*omega_cv*C_out
Ki_v        = 0.1*(omega_cv**2)*C_out
