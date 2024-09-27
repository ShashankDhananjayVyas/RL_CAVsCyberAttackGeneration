import numpy as np
import scipy
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO
import matplotlib.pyplot as plt
import pickle
import EnvVeh

""" Simulation conditions """
# Leader vehicle's velocity and acceleration data
zcfile = scipy.io.loadmat('UDDS_Profile_repeated.mat')
t = zcfile['t']
vL = zcfile['vL']
dt = t[0,1] - t[0,0]
Nsim = t.shape[1] # Nsim = 271802
zc = np.zeros((2,Nsim), dtype=np.float32)
for i in range(0, Nsim-1):
    zc[0,i] = vL[0,i]
    zc[1,i] = (vL[0,i+1] - vL[0,i])/dt
zc[0,Nsim-1] = vL[0,Nsim-1]
zc[1,Nsim-1] = zc[1,Nsim-2]

# Initial condition for ego vehicle
x0 = np.array([[5],[0],[0]], dtype=np.float32)

# Maximum time steps to train the agent
max_timesteps = int(3e5)

# Total number of episodes to simulate
total_episodes = Nsim - 1

""" RL environment """
env = EnvVeh.env(zc, dt, x0, Nsim)
check_env(env)

""" RL agent definition and training """
# agent = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./logs/")
# agent.learn(total_timesteps=max_timesteps, progress_bar=True, tb_log_name=f"PPO_{max_timesteps}", reset_num_timesteps=False)
# agent.save(f"./agents/PPO_{max_timesteps}")
agent = PPO.load(f"./agents/PPO_{max_timesteps}", env=env)

""" Resetting the environment """
state, info = env.reset()

""" Variables for analyzing the results """
# State variables
x = state
# Reward
rwrd = []

# Taking one step in the environment for initializing input output variables
action, _UNUSEDstates = agent.predict(state)
state, reward, terminated, truncated, info = env.step(action)
x = np.append(x, state, axis=1)
rwrd = np.append(rwrd, reward)

# Input output variables
[y_att, y, y_sens, u_ctrl, u_att, u] = \
    [info['y_att'], info['y'], info['y_sens'], info['u_ctrl'], info['u_att'], info['u']]
th = info['th'] # Bounds on states for detection and physical limits

""" Agent performance """
for iter_episode in range(total_episodes):
    action, _UNUSEDstates = agent.predict(state)
    state, reward, terminated, truncated, info = env.step(action)
    x = np.append(x, state, axis=1)
    y_att = np.append(y_att, info['y_att'], axis=1)
    y = np.append(y, info['y'], axis=1)
    y_sens = np.append(y_sens, info['y_sens'], axis=1)
    u_ctrl = np.append(u_ctrl, info['u_ctrl'])
    u_att = np.append(u_att, info['u_att'])
    u = np.append(u, info['u'])
    rwrd = np.append(rwrd, reward)
    print(f"Reward = {reward}")
    print(f"Distance between the vehicles = {state[0,0]}")
    print(f"Velocity of ego vehicle = {state[1, 0]}")
    print(f"Acceleration of ego vehicle = {state[2, 0]}")
    if terminated or truncated:
        state, info = env.reset()
        print(f"Number of time steps required to collide : {iter_episode}")
        print(f"x.shape={x.shape}, y_sens.shape={y_sens.shape}, u.shape={u.shape}")
        break

""" Making variables sizes compatible """
u_ctrl = np.reshape(u_ctrl, (1, iter_episode+2))
u_att = np.reshape(u_att, (1, iter_episode+2))
u = np.reshape(u, (1, iter_episode+2))

""" Saving the variables """
var_list = [t, zc, x, iter_episode, y_att, y, y_sens, u_ctrl, u_att, u, th]
var_dict = {'t':t, 'zc':zc, 'x':x, 'iter':iter_episode,
            'y_att':y_att, 'y':y, 'y_sens':y_sens, 'u_ctrl':u_ctrl, 'u_att':u_att, 'u':u, 'th':th}
reward_dict = {'R':rwrd}
# fdatapy = open('datapy.pckl', 'wb')
# pickle.dump(var_list, fdatapy)
# fdatapy.close()
# scipy.io.savemat("datamat.mat", var_dict)
# scipy.io.savemat("/Users/dragon_shanks/Library/CloudStorage/OneDrive-ThePennsylvaniaStateUniversity"
#                  "/PSU_acad/PhD/06_adversarial_modeling_platoons_RL/datamat.mat", var_dict)
# scipy.io.savemat("reward.mat", reward_dict)
# scipy.io.savemat("/Users/dragon_shanks/Library/CloudStorage/OneDrive-ThePennsylvaniaStateUniversity"
                 # "/PSU_acad/PhD/06_adversarial_modeling_platoons_RL/reward.mat", reward_dict)

""" Plotting the results """
# exec(open("plotspy.py").read())

""" Closing the environment """
env.close()

