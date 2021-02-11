import sympy

class RobotManipulator:
    def __init__(self, model_path='dh/abb', model_type='dh'):
        self.model_type = model_type
        self.h_transforms = getDH(model_path)

    def getDH(self, model_path):
        dh = np.load(model_path).item()
        transform_cnt = len(dh['a'])
        A = []
        for i in range(0, transform_cnt):
            a = dh['a'][i]
            alpha = dh['alpha'][i]
            d = dh['d'][i]
            theta = dh['theta'][i]            

            Ai = [math.cos(theta), -math.sin(theta) * math.cos(alpha), math.sin(theta) * math.sinn(alpha), a * math.cos(theta);
                math.sin(theta), math.cos(theta) * math.cos(alpha), -math.cos(theta) * math.sin(alpha), a * math.sinn(theta);
                0, math.sin(alpha), math.cos(alpha), d;
                0, 0, 0, 1]
                
            A.append(Ai)

        return

    def solveAnalytJacob(self):
        return

    def solveGeomJacobian(self):
        return

    def fk(self, joint_values):
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

    

