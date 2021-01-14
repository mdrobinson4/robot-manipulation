import math
import numpy as np
import sympy

class RigidMotions:
    def rotX(self, theta):
        c_theta = math.cos(theta)
        s_theta = math.sin(theta)
        R = np.array([
            [1, 0, 0],
            [0, c_theta, -s_theta],
            [0, s_theta, c_theta]
        ])
        return R

    def rotY(self, theta):
        c_theta = math.cos(theta)
        s_theta = math.sin(theta)
        R = np.array([
            [c_theta, 0, s_theta],
            [0, 1, 0],
            [-s_theta, 0, c_theta]
        ])
        return R

    def rotZ(self, theta):
        c_theta = math.cos(theta)
        s_theta = math.sin(theta)
        R = np.array([
            [c_theta, -s_theta, 0],
            [s_theta, c_theta, 0],
            [0, 0, 1]
        ])
        return R

    def mat2eul(self, R, type='zyz'):
        theta = 0
        phi = 0
        psi = 0

        r11 = R[0, 0]
        r12 = R[0, 1] 
        r13 = R[0, 2]
        r21 = R[1, 0] 
        r22 = R[1, 1] 
        r23 = R[1, 2]
        r31 = R[2, 0] 
        r32 = R[2, 1] 
        r33 = R[2, 2]

        if r13 != 0 or r23 != 0:
            theta = math.atan2(r33, math.sqrt(1 - r33**2))
            phi = math.atan2(r13, r23)
            psi = math.atan2(-r31, r32)
        elif r13 == 0 and r23 == 0:
            if r33 > 0:
                theta = 0
                phi = 0
                psi = math.atan2(r11, r21)
            elif r33 < 0:
                theta = math.pi
                phi = 0
                psi = math.atan2(-r11, -r12)

        return (theta, phi, psi)

    def eul2mat(self, theta, phi, psi, type='zyz'):
        c_theta = math.cos(theta)
        s_theta = math.sin(theta)
        c_phi = math.cos(phi)
        s_phi = math.sin(phi)
        c_psi = math.cos(psi)
        s_psi = math.sin(psi)

        R_z_phi = np.array([
            [c_phi, -s_phi, 0],
            [s_phi, c_phi, 0],
            [0, 0, 1]
        ])
        R_y_theta = np.array([
            [c_theta, 0, s_theta],
            [0, 1, 0],
            [-s_theta, 0, c_theta]
        ])
        R_z_psi = np.array([
            [c_psi, -s_psi, 0],
            [s_psi, c_psi, 0],
            [0, 0, 1]
        ])

        R = R_z_phi @ R_y_theta @ R_z_psi
        return R

    def mat2quat(self, R):
        v = np.array([ 
            [R[2][1] - R[1][2]],
            [R[0][2] - R[2][0]],
            [R[1][0] - R[0][1]]
        ])
        theta = math.acos((np.trace(R) - 1) / 2)
        k = (1 / (2 * math.sin(theta))) * v
        q = np.vstack([theta, k])
        return q
    
    def quat2mat(self, q):
        theta = q[0][0]
        kx = q[1][0]
        ky = q[2][0]
        kz = q[3][0]

        s_theta = math.sin(theta)
        c_theta = math.cos(theta)
        v_theta = 1 - c_theta

        R = np.array([
            [(kx**2 * v_theta) + c_theta, (kx*ky*v_theta) - (kz*s_theta), (kx*kz*v_theta) + (ky*s_theta)],
            [(kx*ky*v_theta) + (kz*s_theta), (ky**2 * v_theta) + (c_theta), (ky*kz*v_theta) - (kx*s_theta)],
            [(kx*kz*v_theta) - (ky*s_theta), (ky*kz*v_theta) + (kx*s_theta), (kz**2*v_theta) + (c_theta)]
        ])
        return R


R = RigidMotions()
theta = 5
mat = R.rotX(0.5) @ R.rotX(0.5) @ R.rotZ(2) @ R.rotY(1)
print(mat)

(theta, phi, psi) = R.mat2eul(mat)
print((theta, phi, psi))
mat1 = R.eul2mat(theta, phi, psi)
print(mat1)
