from motion_profile import MotionProfile
import numpy as np
import matplotlib.pyplot as plt

profile = MotionProfile(20, 4, 100)
print(profile.duration)
time = np.arange(0, 15000, 1)
accels = np.zeros(15000)
for i in range(15000):
  accels[i] = profile.get_pos(i/1000)

plt.plot(time, accels)
plt.show()


