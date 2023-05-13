from motion_profile import MotionProfile
import time
import pygame
import matplotlib.pyplot as plt
import numpy as np

profile = MotionProfile(30, 6, 75)

clock = pygame.time.Clock()
dt = 0

pygame.init()
screen = pygame.display.set_mode((1700, 600))
robot = pygame.Rect((200, 280, 40, 40))
time = 0

running = True
while running:
  screen.fill((0,0,0))
  pygame.draw.rect(screen, (0,255,0), robot)
  pygame.draw.line(screen, (255,0,0),(200,280), (500,280), 3)
  time += dt
  pos_change = profile.get_vel(time) * dt
  robot.move_ip(pos_change * 4, 0)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.update()

  dt = clock.tick(60)/1000
pygame.quit()


