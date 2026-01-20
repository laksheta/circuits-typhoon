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
V_g = 220 * np.sqrt(2)
V_rms = 220
F = 50

phase = np.array([0,-120,120])

L = 1e-3
R = L / tau

I_amp = 10
I_angle_deg = 0
I_angle_rad = np.deg2rad(I_angle_deg)

I_x = I_amp * np.cos(I_angle_rad)
I_y = I_amp * np.sin(I_angle_rad)

V_R_amp = I_amp * R
V_R_x = V_R_amp * np.cos(I_angle_rad)
V_R_y = V_R_amp * np.sin(I_angle_rad)

V_g_x = V_g

x_L = 2 * np.pi * F * L

V_L_amp = I_amp * x_L
V_L_angle = I_angle_rad + 0.5 * np.pi
V_L_x = V_L_amp * np.cos(V_L_angle)
V_L_y = V_L_amp * np.sin(V_L_angle)

V_inv_x = V_R_x + V_g_x + V_L_x
V_inv_y = V_R_y + V_L_y
V_inv = np.sqrt(V_inv_x**2 + V_inv_y**2)
U_inv_rms = V_inv / np.sqrt(2)

angle = np.arctan2(V_inv_y, V_inv_x)
angle_deg = np.rad2deg(angle)

phase_inv = phase + angle_deg

info(f"V_inv (Peak Voltage): {V_inv:.2f} V")
info(f"U_inv_rms (RMS Voltage): {U_inv_rms:.2f} V")
info(f"Phase Angle (Deg): {angle_deg:.2f} °")
info(f"Phase Angle Matrix: {phase_inv:} °")

info(f"d_inv: {V_inv_x:.2f}")
info(f"q_inv: {V_inv_y:.2f}")
