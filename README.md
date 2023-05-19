# robot_sim
## Constant-Acceleration Motion Profiles
![Constant-Acceleration Motion Profile](/assets/Figure_1.png)
### Usage
    #Create the profile
    max_vel = 5
    max_acc = 20
    final_position = 200
    profile = new MotionProfile(max_vel, max_accel, final_position)

    #Use the profile
    time = 3 #seconds
    profile.get_pos(time) --> double
    profile.get_vel(time) --> double
    profile.get_acc(time) --> double