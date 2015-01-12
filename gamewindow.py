import os, sys, math, pygame, pygame.mixer
from pygame.mixer import *
#the following line will be where we import files from our project.


# defining some basic colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0,
green = 0, 255, 0,
blue = 0, 0, 255

# Defining the screen size
screen_size = screen_width, screen_height = 600, 400

#Setting the display and getting the Surface object
screen = pygame.display.set_mode(screen_size)
#Getting the Clock object
clock = pygame.time.Clock()
#Setting a title to the Window
pygame.display.set_caption('PONG by LHS programming club')

#defining variables for fps and continued running
fps_limit = 60
run_me = True
while run_me:
  #limit the framerate
  clock.tick(fps_limit)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run_me = False
  #Clear the screen
  screen.fill(white)
  
  #Display everything in the screen.
  pygame.display.flip()

#Quit the game
pygame.quit()
sys.exit()
