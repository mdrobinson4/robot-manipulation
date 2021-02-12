import pickle
import sympy
import os
import numpy as np
  
if __name__ == '__main__': 
    th1, th2, th3, th4, th5, th6 = sympy.symbols("th1, th2, th3, th4, th5, th6")
    
    abb_robot_dh = {
        'a': [0, -90, 0, -90, 90, -90],
        'alpha': [0, 320, 975, 280, 0, 0],
        'd': [0, 0, 0, 887, 0, 0],
        'theta': [th1, th2, th3, th4, th5, th6],
        'type': ['r', 'r', 'r', 'r', 'r', 'r']
    }

    fanuc_robot_dh = {
        'a': [0, -90, 0, -90, 90, -90],
        'alpha': [0, 500, 1700, 180, 0, 0],
        'd': [0, 0, 0, 2850, 0, 0],
        'theta': [th1, th2, th3, th4, th5, th6],
        'type': ['r', 'r', 'r', 'r', 'r', 'r']
    }

    np.save('dh/abb.npy', abb_robot_dh)
    np.save('dh/fanuc.npy', fanuc_robot_dh)