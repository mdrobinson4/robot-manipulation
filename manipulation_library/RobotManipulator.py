import sympy
import numpy as np
import math

class RobotManipulator:
    def __init__(self, model_path='dh/abb.npy', model_type='dh'):
        self.model_type = model_type
        self.theta = [sympy.symbols("th1, th2, th3, th4, th5, th6")]
        self.HT, self.joint_type = self.getDH(model_path)

    def getDH(self, model_path):
        dh = np.load('dh/abb.npy', allow_pickle=True).item()
        transform_cnt = len(dh['a'])
        A = []
        joint_type = []
        for i in range(0, transform_cnt):
            a = dh['a'][i]
            alpha = dh['alpha'][i]
            d = math.radians(dh['d'][i])
            theta = dh['theta'][i]            

            Ai = sympy.Matrix([
                    [sympy.cos(theta), -sympy.sin(theta) * sympy.cos(alpha), sympy.sin(theta) * sympy.sin(alpha), a * sympy.cos(theta)],
                    [sympy.sin(theta), sympy.cos(theta) * sympy.cos(alpha), -sympy.cos(theta) * sympy.sin(alpha), a * sympy.sin(theta)],
                    [0, sympy.sin(alpha), sympy.cos(alpha), d],
                    [0, 0, 0, 1]
            ])
            
            if len(A) > 0:
                Ai = A[-1] * Ai
            A.append(Ai)
            joint_type.append(dh['type'][i])
        return A, joint_type

    def fk(self, joint_values):
        f = sympy.lambdify(self.theta, self.HT[1], 'numpy')
        T = f(joint_values)
        return T

    def computeJacobian(self):
        jvi = None
        jwi = None
        Jv = sympy.zeros(3, 6)
        Jw = sympy.zeros(3, 6)
        o_n = self.HT[-1][0:3, 3]
        for i in range(1, len(self.HT) + 1):
            z = self.HT[i - 1][0:3, 3]
            if self.joint_type[i-1] == 'r':
                do = self.HT[-1][0:3, 3] - self.HT[i - 1][0:3, 3]
                jvi = z.cross(do)
            else:
                jvi = z
            if self.joint_type[i-1] == 'r':
                jwi = z
            else:
                jwi = np.zeros((3, 1))
            Jv[0:3, i-1] = jvi
            Jw[0:3, i-1] = jwi

    def solveAnalytJacob(self):
        return

    def solveGeomJacobian(self):
        return

    def fvk(self, joint_values):
        return

    def fak(self, joint_values):
        return
    
    def ik(self, ee_position, solver='analytical'):
        return

    def ivk(self, ee_position, solver='analytical'):
        return

    def iak(self, ee_position, solver='analytical'):
        return

    def jointSpaceTrajectory():
        return

    def taskSpaceTrajectory():
        return

    def getLagrange(self):
        return
    
    def getNewtonEuler(self):
        return
    
    def pdControl(self):
        return

    def pidControl(self):
        return
    
    def computedTorqueControl(self):
        return

    

