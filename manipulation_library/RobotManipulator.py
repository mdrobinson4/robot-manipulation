import sympy
import numpy as np
import math

class RobotManipulator:
    def __init__(self, model_path='dh/abb.npy', model_type='dh'):
        self.model_type = model_type
        self.theta = [sympy.symbols("th1, th2, th3, th4, th5, th6")]
        self.ht = self.getDH(model_path)

    def getDH(self, model_path):
        dh = np.load('dh/abb.npy', allow_pickle=True).item()
        transform_cnt = len(dh['a'])
        A = []
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
        return A

    def fk(self, joint_values):
        f = sympy.lambdify(self.theta, self.ht[1], 'numpy')
        T = f(joint_values)
        return T

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

    

