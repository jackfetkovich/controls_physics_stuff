import sys
sys.path.append('/home/jack/Documents/control_sim_stuff')

from motion_profile import MotionProfile
import math
import time
import pygame
import matplotlib.pyplot as plt
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1200, 600))
for i in range(100):
  profile = MotionProfile(65, 30, 200)

  clock = pygame.time.Clock()
  dt = 0

  start = 0
  x_goal = 0
  x_cur = start
  last = 0


  robot = pygame.Rect((start, 280, 40, 40))
  time = 0


  running = True
  while running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,255,0), robot)
    pygame.draw.line(screen, (255,0,0),(start,280), (800 + 40,280), 3)
    time += dt

    # 1px = 2 distance units
    x_goal = profile.get_pos(time)
    x_cur = round(float(x_goal)/0.5) + start
    robot.move_ip(2*(x_cur - last), 0)
    print(x_cur)
    last = x_cur

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    pygame.display.update()

    dt = clock.tick(60)/1000
pygame.quit()


