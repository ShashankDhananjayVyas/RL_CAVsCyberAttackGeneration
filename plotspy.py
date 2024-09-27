""" Plotting the results """
# Inputs: u_ctrl, u_att, u
fig1, axs1 = plt.subplots(2, 1)
axs1[0].plot(t[0:1,0:iter_episode+2], u_ctrl, 'g', t[0:1,0:iter_episode+2], u, 'r',
             t[0:1,0:iter_episode+2], -th[2,0]*np.ones(u.shape), 'k--', t[0:1,0:iter_episode+2], th[2,0]*np.ones(u.shape), 'k--')
axs1[0].legend(['u_ctrl : as determined by the controller', 'u : as sent by the controller'])
axs1[1].plot(t[0:1,0:iter_episode+2], u_att, 'k',
             t[0:1,0:iter_episode+2], -th[2,0]*np.ones(u.shape), 'k--', t[0:1,0:iter_episode+2], th[2,0]*np.ones(u.shape), 'k--')
axs1[1].set(ylabel='u_att : input attack profile')

# Output: y, y_att, y_sens
fig2, axs2 = plt.subplots(3, 2)
# Inter-vehicular distance
axs2[0,0].plot(t[0:1,0:iter_episode+2], y_sens[0:1], 'g', t[0:1,0:iter_episode+2], y[0:1], 'r',
               t[0:1,0:iter_episode+2], th[0,0]*np.ones(y[0:1].shape), 'k--', t[0:1,0:iter_episode+2], 0*np.ones(y[0:1].shape), 'k--')
axs2[0,0].legend(['y_sens : sensor outputs', 'y : actual vehicle states'])
axs2[0,1].set(ylabel='d [m]')
axs2[0,1].plot(t[0:1,0:iter_episode+2], y_att[0:1], 'k')
axs2[0,1].legend(['y_att : output attack profiles'])
axs2[0,1].set(ylabel='d [m]')
# Ego vehicle velocity
axs2[1,0].plot(t[0:1,0:iter_episode+2], y_sens[1:2], 'g', t[0:1,0:iter_episode+2], y[1:2], 'r',
               t[0:1,0:iter_episode+2], 0*np.ones(y[1:2].shape), 'k--', t[0:1,0:iter_episode+2], th[1,0]*np.ones(y[1:2].shape), 'k--')
# axs2[1,0].legend(['y_sens = v : as measured by the sensor', 'y = v : actual vehicle output'])
axs2[0,1].set(ylabel='v [m/s]')
axs2[1,1].plot(t[0:1,0:iter_episode+2], y_att[1:2], 'k')
axs2[0,1].set(ylabel='v [m/s]')
# Ego vehicle acceleration
axs2[2,0].plot(t[0:1,0:iter_episode+2], y_sens[2:3], 'g', t[0:1,0:iter_episode+2], y[2:3], 'r',
               t[0:1,0:iter_episode+2], -th[2,0]*np.ones(y[2:3].shape), 'k--', t[0:1,0:iter_episode+2], th[2,0]*np.ones(y[2:3].shape), 'k--')
# axs2[2,0].legend(['y_sens = a : as measured by the sensor', 'y = a : actual vehicle output'])
axs2[0,1].set(ylabel='a [m/s^2]')
axs2[2,1].plot(t[0:1,0:iter_episode+2], y_att[2:3], 'k')
axs2[0,1].set(ylabel='a [m/s^2]')

plt.show()