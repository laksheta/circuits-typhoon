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

