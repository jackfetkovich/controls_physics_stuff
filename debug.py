from motion_profile import MotionProfile

profile = MotionProfile(20, 4, 1000)
time = 2
time *= 1000
print(profile.get_pos(time))
print(time)
print(int(time))
print(profile.pos[int(time)])