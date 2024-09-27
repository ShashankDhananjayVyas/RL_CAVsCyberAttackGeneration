import numpy as np

""" Vehicle local controller parameters h, kp and kd """
h = 0.6
# h = 0.6*0.95 #hm
# h = 0.6*1.05 #hp
kp = 0.7
# kp = 0.7*0.95 #kpm
# kp = 0.7*1.05 #kpp
kd = 1.0
# kd = 1.0*0.95 #kdm
# kd = 1.0*1.05 #kdp

""" Matrices for vehicle dynamics consisting of 3 states x=[d, v, a]' """
A = np.zeros((3,3))
A[0,1] = -1
A[1,2] = 1
A[2,2] = -1/h
B = np.array([[0], [0], [1/h]])
C1 = np.zeros((3,2))
C1[0,0] = 1
C = np.eye(3)
C2 = np.array([[kp, -(kp*h+kd), -kd*h]])
C3 = np.array([[kd, 1]])

""" Target state coefficients """
refd = -1.0
refv = 1.0
refa = 10.0

