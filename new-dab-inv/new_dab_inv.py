import numpy as np

#################
#################
#######DAB#######
#################
#################

fsw_dab = 10e3

T_plant_dab = 1e-6
T_meas_dab = 1e-6
T_wave_dab  = 1e-6 
T_math_dab  = 1e-6

V_in_dab  = 780
V_out_dab = 780
V1_dab  = 780
V2_dab  = 780
C_dab   = 1e-6

n_dab   = 1

P_dab   = 10e3
D_dab   = 0.5
L_dab   = (V1_dab * V2_dab) * D_dab * (1 - D_dab) / (2 * fsw_dab * P_dab)

d_dab   = 0.25
deg_dab = d_dab * (90 / 0.5)
phi_dab = (deg_dab / 360) * (1 / fsw_dab)

phi_pu_dab = 1 - phi_dab * fsw_dab

I_dab = V1_dab * D_dab * (1 - D_dab) / (2 * fsw_dab * L_dab)
R_load_dab = V1_dab / I_dab

P_c_dab = 5e3
R_load_c_dab  = (V_out_dab ** 2) / P_c_dab 

d_c_dab = d_dab * 0.5

Gdc_dab     = ((R_load_c_dab) / (2 * V_out_dab)) * ((V1_dab * V2_dab * (1 - 2 * d_c_dab) / (2 * fsw_dab * L_dab)))
tau_dab     = (C_dab * R_load_c_dab) / 2

f_bw_dab    = 0.05 * fsw_dab
omega_c_dab = 2 * np.pi * f_bw_dab

K_p_dab      = (tau_dab * omega_c_dab) / Gdc_dab
K_i_dab      = K_p_dab / tau_dab

    
#################
#################
#####Inverter####
#################
#################

T_plant_inv = 50e-6
T_math_inv = 100e-6
T_meas_inv = 100e-6

tau_inv = 1e-3

V_dc_inv = 780
upper_lim_inv = +V_dc_inv/2
lower_lim_inv = -V_dc_inv/2

V_g_inv = 220 * np.sqrt(2)
V_rms_inv = 220
u_grid_d_inv  = 220*np.sqrt(2)
V_peak_inv    = u_grid_d_inv
u_grid_q_inv  = 0
u_grid_amp_inv    = np.sqrt(u_grid_d_inv**2+u_grid_q_inv**2)
u_grid_ph_inv     = np.arctan2(u_grid_q_inv, u_grid_d_inv)

F_inv = 50
phase_inv = np.array([0,-120,120])

L_inv = 1e-3
R_inv = L_inv / tau_inv

i_d_inv = 10
i_q_inv = 0
omega_inv   = 2*np.pi*F_inv

u_d_inv = u_grid_d_inv + R_inv*i_d_inv - omega_inv*L_inv*i_q_inv
u_q_inv = u_grid_q_inv + R_inv*i_q_inv + omega_inv*L_inv*i_d_inv

U_inv_amp_inv = np.sqrt(u_d_inv**2+u_q_inv**2)
U_inv_ph_inv  = np.arctan2(u_q_inv, u_d_inv)

f_wb_i_inv = 1e3
omega_c_inv = 2*np.pi*f_wb_i_inv

Kp_i_inv    = omega_c_inv*L_inv
Ki_i_inv    = omega_c_inv*R_inv

