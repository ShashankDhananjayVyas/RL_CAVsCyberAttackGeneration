import numpy as np
import parameters as param

def dynamics(state, action, comm_inp, dt):
        x = state
        # u_att = action
        u_att = action[0:1]
        y_att = action[1:4]
        # y_att = np.zeros((3,1))
        zc = comm_inp
        y = param.C @ x
        y_sens = y + y_att
        u_ctrl = param.C2 @ y_sens + param.C3 @ zc
        u = u_ctrl + u_att
        x = (dt * param.A + np.eye(3)) @ x + dt * u * param.B + dt * param.C1 @ zc
        x = np.float32(x)
        return y_att, y, y_sens, u_ctrl, u_att, u, x

