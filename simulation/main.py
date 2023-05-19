from motion_profile import MotionProfile
import time
import pygame
import matplotlib.pyplot as plt
import numpy as np

profile = MotionProfile(60, 22, 400)

clock = pygame.time.Clock()
dt = 0

x_buffer = 0
pygame.init()
screen = pygame.display.set_mode((1700, 600))
robot = pygame.Rect((200, 280, 40, 40))
time = 0


running = True
while running:
  screen.fill((0,0,0))
  pygame.draw.rect(screen, (0,255,0), robot)
  pygame.draw.line(screen, (255,0,0),(200,280), (600,280), 3)
  time += dt
  x_buffer += profile.get_vel(time) * dt
  print(x_buffer)
  dx = x_buffer - x_buffer % 1 if x_buffer > 1 else 0
  x_buffer = x_buffer if dx == 0 else x_buffer - x_buffer % 1
  print(dx)

  robot.move_ip(dx, 0)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.update()

  dt = clock.tick(60)/1000
pygame.quit()


