import numpy as np
import math

class MotionProfile:
  def __init__(self, max_vel, max_accel, final_pos, current_pos=0):
    time_to_max_vel = (max_vel / max_accel) * 1000
    accel_dist = max_accel * (time_to_max_vel/1000)**2
    remaining_dist = final_pos - current_pos - accel_dist
    time_in_max_vel = (remaining_dist / max_vel) * 1000
    
    if 2*accel_dist > final_pos - current_pos:
      time_to_max_vel = math.sqrt(2 * accel_dist / max_accel) * 1000
      time_in_max_vel = 0

    profile_time = 2 * time_to_max_vel + time_in_max_vel


    self.pos = np.zeros(round(profile_time), dtype="float")
    self.vels = np.zeros(round(profile_time), dtype="float")
    self.accels = np.zeros(round(profile_time),dtype="float")
    self.duration = profile_time

    for time in range(round(profile_time)):
      if time < time_to_max_vel:
        self.accels[time] = max_accel * (abs(final_pos - current_pos) / (final_pos - current_pos))
      elif time > time_in_max_vel + time_to_max_vel:
        self.accels[time] = -max_accel* (abs(final_pos - current_pos) / (final_pos - current_pos))
      else:
        self.accels[time] = 0
      self.vels[time] = self.vels[time - 1] + self.accels[time]/1000
      self.pos[time] = self.pos[time - 1] + self.vels[time]/1000

  def get_pos(self, time):
    time *= 1000
    time = int(time)
    time = time if time <= self.duration else round(self.duration)-1
    return self.pos[time]

  def get_vel(self, time):
    time *= 1000
    time=int(time)
    time = time if time <= self.duration else round(self.duration)-1
    return self.vels[time]
  
  def get_acc(self, time):
    time *= 1000
    time=int(time)
    time = time if time <= self.duration else round(self.duration)-1
    return self.accels[time]