from motion_profile import MotionProfile
import numpy as np
import matplotlib.pyplot as plt

profile = MotionProfile(20, 2, 450)
increments = int(profile.duration * 1000)
time = np.arange(0, increments, 1)
accels = np.zeros(increments)
vels = np.zeros(increments)
pos = np.zeros(increments)

for i in range(increments):
  accels[i] = profile.get_acc(i/1000)
  vels[i] = profile.get_vel(i/1000)
  pos[i] = profile.get_pos(i/1000)

plt.figure(1)
plt.subplot(311)
plt.plot(time, pos)

plt.subplot(312)
plt.plot(time, vels)

plt.subplot(313)
plt.plot(time, accels)

plt.show()