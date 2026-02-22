import numpy as np

#################
#################
#######DAB#######
#################
#################

fsw_dab = 10e3
T_dab = 1/fsw_dab

T_meas_dab = 0.1e-6
T_wave_dab  = 1e-6  
T_math_dab  = 0.1e-6
T_delay_dab = 1e-6
T_plant_dab = 1e-6

delay_deg_dab   = 45
delay_N_dab = ((delay_deg_dab/360)*T_dab)/T_delay_dab

V_in_dab  = 780
V_out_dab = 780
V1_dab  = 780
V2_dab  = 780
C_dab   = 1000e-6

P_dab   = 10e3
D_dab   = 0.5
L_dab   = (V1_dab*V2_dab)*D_dab*(1-D_dab)/(2*fsw_dab*P_dab)

d_dab   = 0.5
deg_dab = d_dab*(90/0.5)
phi_dab = (deg_dab/360)*(1/fsw_dab)

phi_pu_dab = 1-phi_dab*fsw_dab

I_dab = V1_dab*D_dab*(1-D_dab)/(2*fsw_dab*L_dab)
R_load_dab = V1_dab/I_dab

P_c_dab = 5e3
R_load_c_dab  = (V_out_dab**2) / P_c_dab 

d_c_dab = d_dab*0.5

Gdc_dab     = ((R_load_c_dab)/(2*V_out_dab))*((V1_dab*V2_dab*(1-2*d_c_dab)/(2*fsw_dab*L_dab)))
tau_dab     = (C_dab*R_load_c_dab)/2

f_bw_dab    = 0.05*fsw_dab
omega_c_dab = 2*np.pi*f_bw_dab

K_p_dab      = (tau_dab*omega_c_dab)/Gdc_dab
K_i_dab      = K_p_dab/tau_dab



    
#################
#################
#####Inverter####
#################
#################

if 'info' not in globals():
    info = print

sig_select_inv = [1]

T_meas_inv = 1e-6
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

info(f"u_d_inv: {u_d_inv:.2f}")
info(f"u_q_inv: {u_q_inv:.2f}")


# Numpy module is imported as 'np'
# Scipy module is imported as 'sp'
# The Schematic API is imported as 'mdl'
# To get the model file path, use 'mdl.get_model_file_path()'
# To print information to the console, use info()
import numpy as np

if 'info' not in globals():
    info = print

# sig_select = [1]

# T_meas = 1e-6
# tau = 1e-3

# V_dc = 780
# upper_lim = +V_dc/2
# lower_lim = -V_dc/2

# V_g = 220 * np.sqrt(2)
# V_rms = 220
# u_grid_d  = 220*np.sqrt(2)
# V_peak    = u_grid_d
# u_grid_q  = 0
# u_grid_amp    = np.sqrt(u_grid_d**2+u_grid_q**2)
# u_grid_ph     = np.arctan2(u_grid_q, u_grid_d)

# F = 50
# phase = np.array([0,-120,120])

L = 1e-3
# R = L / tau

i_d = 10
i_q = 0
# omega   = 2*np.pi*F

# u_d = u_grid_d + R*i_d - omega*L*i_q
# u_q = u_grid_q + R*i_q + omega*L*i_d

# U_inv_amp = np.sqrt(u_d**2+u_q**2)
# U_inv_ph  = np.arctan2(u_q, u_d)

f_wb_i = 1e3
omega_c = 2*np.pi*f_wb_i

Kp_i    = omega_c*L
# Ki_i    = omega_c*R

# info(f"u_d: {u_d:.2f}")
# info(f"u_q: {u_q:.2f}")
