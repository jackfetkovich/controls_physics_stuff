import matplotlib.pyplot as plt
import numpy as np

max_vel = 8
max_accel = 5
current_pos = 0
final_pos = 50

# all times in ms
time_to_max_vel = (max_vel / max_accel) * 1000
accel_dist = max_accel * (time_to_max_vel/1000)**2
remaining_dist = final_pos - current_pos - accel_dist
time_in_max_vel = (remaining_dist / max_vel) * 1000

profile_time = 2 * time_to_max_vel + time_in_max_vel

pos = np.zeros(round(profile_time), dtype="float")
vels = np.zeros(round(profile_time), dtype="float")
accels = np.zeros(round(profile_time),dtype="float")
times = np.arange(0,round(profile_time), dtype="float")

for time in range(round(profile_time)):
  if time < time_to_max_vel:
    accels[time] = max_accel
  elif time > time_in_max_vel + time_to_max_vel:
    accels[time] = -max_accel
  else:
    accels[time] = 0
  vels[time] = vels[time - 1] + accels[time]/1000
  pos[time] = pos[time - 1] + vels[time]/1000

plt.figure()
plt.subplot(311)
plt.plot(times, pos)
plt.title("Position(m) vs Time(ms)")

plt.subplot(312)
plt.plot(times,vels)
plt.title("Velocity(m/s) vs Time(ms)")

plt.subplot(313)
plt.plot(times,accels)
plt.title("Acceleration(m/s/s) vs Time(ms)")

plt.show()
