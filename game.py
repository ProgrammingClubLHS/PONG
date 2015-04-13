#This is the base class for all objects that will be displayed
game_objects = []
class shape(object):
  #this function adds it to the list of objects to be updated.
  def __init__(self):
    game_objects.append(self)
  def update(self):
  def display(self):
  enabled = False
  def enabling(self,arg):
    enabled = arg
    
class circle(shape):
  
  #Assignment #1 Update the init function to 1. run the old function, and 2. accept and store a radius, and an x position and y positon(in that order).
  #assigned
  #Assignment #2 Make a new method for display, that creates a corresponding circle in the pygame engine.
  #assigned
  
class rectangle(shape):
  #Assignment #3 Update the init function to 1. run the old function, and 2,  accept and store a width, diameter, and an x position and y postion(in that order)
  #Assignment #4 make a new method for display, that creates the corresponding rectangle in the pygame engine.
