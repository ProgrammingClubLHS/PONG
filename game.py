#This is the base class for all objects that will be displayed
game_objects = []
def shape(object):
  def __init__(self):
    game_objects.append(self)
  def update(self):
  def display(self):
  enabled = False
  gamespace = 'null'
  def gs(self,arg):
    enabled = (arg == gamespace)
  def gschange(self,arg):
    gamespace = arg
