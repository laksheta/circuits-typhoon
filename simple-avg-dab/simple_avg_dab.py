# Numpy module is imported as 'np'
# Scipy module is imported as 'sp'
# The Schematic API is imported as 'mdl'
# To get the model file path, use 'mdl.get_model_file_path()'
# To print information to the console, use info()
import numpy as np

fsw = 10e3

V1  = 780
V2  = 780

P   = 10e3
D   = 0.5
L   = (V1*V2)*D*(1-D)/(2*fsw*P)