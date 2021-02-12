from RobotManipulator import RobotManipulator

model_path = 'dh/abb.npy'
robot = RobotManipulator(model_path)

joint_values = [0, 0, 0, 0, 0, 0]
print(robot.fk(joint_values))
robot.computeJacobian()