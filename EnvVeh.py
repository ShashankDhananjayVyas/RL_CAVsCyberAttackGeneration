import gymnasium as gym
from gymnasium import spaces
import numpy as np
import DynVeh

class env(gym.Env):
  metadata = {"render_modes": ["human"], "render_fps": 30}

  def __init__(self, VcAc, DynVeh_dt, StateInit, Nsim):
    super().__init__()
    self.action_space = spaces.Box(low=-10, high=10, shape=(4,1), dtype=np.float32)
    self.observation_space = spaces.Box(low=-np.inf*np.ones((3,1)), high=np.inf*np.ones((3,1)), dtype=np.float32)
    self.zc = VcAc
    self.dt = DynVeh_dt
    self.x0 = StateInit
    self.Nsim = Nsim

  def step(self, action):
    # Vehicle dynamics model for propagating to next state
    i = self.step_counter
    y_att, y, y_sens, u_ctrl, u_att, u, self.state = DynVeh.dynamics(self.state,action,self.zc[:,i:i+1],self.dt)
    self.sens_out = self.state + action[1:4]
    self.step_counter += 1
    Ru = R1 = R2 = R3 = 0.0

    # Agent penalty if vehicles have not collided
    if (self.state[0, 0] >= 0.0):
      R0 = -1*self.state[0,0]
      # Additional penalty if inputs are out of bounds
      if ((abs(u_ctrl) >= 10.0) or (abs(u) >= 10.0)) :
        Ru = -20.0
      # Additional penalty if agent is not stealthy
      if (self.sens_out[0, 0] <= self.threshold[0, 0]):
        R1 = -1.0
      if ((self.sens_out[1, 0] >= self.threshold[1, 0]) or (self.sens_out[1, 0] <= 0)):
        R2 = -1.0
      if (abs(self.sens_out[2, 0]) >= self.threshold[2, 0]):
        R3 = -1.0
      self.reward = float(R0 + Ru + R1 + R2 + R3)

    # Vehicle collision check
    if ((self.state[0,0] < 0.0) or (self.step_counter == self.Nsim)):
      self.terminated = self.truncated = True
    else:
      self.terminated = self.truncated = False

    # Placeholder for 'info'
    info = {'y_att':y_att, 'y':y, 'y_sens':y_sens, 'u_ctrl':u_ctrl, 'u_att':u_att, 'u':u, 'th':self.threshold}

    return self.state, self.reward, self.terminated, self.truncated, info

  def reset(self, seed=None, options=None):
    self.state = self.x0
    self.reward = float(0)
    self.terminated = self.truncated = False
    self.step_counter = 0
    self.sens_out = self.x0
    self.threshold = np.array([[1.0],[45.0],[10.0]])
    info = {}

    return self.state, info

  def render(self):
    pass

  def close (self):
    pass

