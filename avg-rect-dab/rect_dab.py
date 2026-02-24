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
####Rectifier####
#################
#################

import numpy as np

T_plant_rect = 50e-6
T_meas_rect   = 100e-6
T_controller_rect = 100e-6

V_grid_peak_rect = 220*np.sqrt(2)
V_grid_rms_rect  = 220
F_rect           = 50
omega_rect       = 2*np.pi*F_rect

R_rect           = 1e-1
L_rect           = 1e-3

R_load_rect      = 100
C_out_rect       = 10e-6

V_dc_target_rect = 780

P_load_rect = (V_dc_target_rect**2) / R_load_rect

i_d_req_rect = -(2 * P_load_rect) / (3 * V_grid_peak_rect)
i_q_req_rect = 0

u_d_rect = V_grid_peak_rect - (R_rect * i_d_req_rect - omega_rect * L_rect * i_q_req_rect)
u_q_rect = 0 - (R_rect * i_q_req_rect + omega_rect * L_rect * i_d_req_rect)

U_rect_amp_rect = np.sqrt(u_d_rect**2 + u_q_rect**2)
U_rect_rms_rect = U_rect_amp_rect/np.sqrt(2)
delta_rad_rect  = np.arctan2(u_q_rect, u_d_rect)
delta_rect      = delta_rad_rect * (180/np.pi)

m_rect = U_rect_amp_rect / V_dc_target_rect

phase_rect = [0+delta_rect, -120+delta_rect, 120+delta_rect]
phase_3ph_rect    = delta_rect

V_rect = m_rect*V_dc_target_rect

# Controller
f_bw_i      = 1e3
omega_ci    = 2*np.pi*f_bw_i
Kp_i        = omega_ci * L_rect
Ki_i        = omega_ci * R_rect

f_bw_v      = 20
omega_cv    = 2*np.pi*f_bw_v
zeta        = 0.707
Kp_v        = 2*zeta*omega_cv*C_out_rect
Ki_v        = (omega_cv**2)*C_out_rect
