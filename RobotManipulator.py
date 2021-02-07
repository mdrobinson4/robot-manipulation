import sympy

class RobotManipulator:
    def __init__(self, model_path, model_type='dh'):
        self.model_type = model_type
        self.h_transforms = getDH(model_path)

    def getDH(self, model_path):
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

    

