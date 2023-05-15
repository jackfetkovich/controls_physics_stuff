import numpy as np
import math

class MotionProfile:
  def __init__(self, max_vel, max_accel, final_pos, current_pos=0):
    self.time_to_max_vel = (max_vel / max_accel)
    self.accel_dist = max_accel * (self.time_to_max_vel)**2
    self.remaining_dist = final_pos - current_pos - self.accel_dist
    self.time_in_max_vel = (self.remaining_dist / max_vel) 
    
    if 2*self.accel_dist > final_pos - current_pos:
      self.time_to_max_vel = math.sqrt(2 * self.accel_dist / max_accel)
      self.time_in_max_vel = 0

    profile_time = 2 * self.time_to_max_vel + self.time_in_max_vel

    self.max_vel = max_vel
    self.max_accel = max_accel
    self.final_pos = final_pos
    self.current_pos = current_pos
    self.duration = profile_time
    self.direction = abs(self.final_pos - self.current_pos) / (self.final_pos - self.current_pos)

  def get_pos(self, time):
    if time <= self.time_to_max_vel:
      return 0.5 * self.max_accel * time**2 * self.direction
    elif time > self.time_to_max_vel and time <= self.time_in_max_vel + self.time_to_max_vel:
      return self.get_pos(self.time_to_max_vel) + self.get_vel(time) * (time - self.time_to_max_vel)
    elif time < self.duration:
      # DVAT???
      return self.get_pos(self.time_in_max_vel + self.time_to_max_vel) + self.get_vel(time) * (time - self.time_in_max_vel - self.time_to_max_vel) + 0.5 * self.max_accel* self.direction * (time - self.time_in_max_vel - self.time_to_max_vel)**2 
    else:
      return self.final_pos

  def get_vel(self, time):
    if time < self.time_to_max_vel:
      return self.get_acc(time) * time
    elif time > self.time_in_max_vel + self.time_to_max_vel and time < self.duration:
      return self.max_vel * self.direction + self.get_acc(time)*(time-self.time_to_max_vel-self.time_in_max_vel)
    elif time < self.duration:
      return self.max_vel * self.direction
    else: 
      return 0
  
  def get_acc(self, time):
    if time < self.time_to_max_vel:
      return self.max_accel * self.direction
    elif time > self.time_in_max_vel + self.time_to_max_vel and time < self.duration:
      return -self.max_accel * self.direction
    else:
      return 0