import pygame, sys
from pygame.locals import *
import math
import keys
import game_engine
import collisions

player_image = pygame.image.load( "img/Bulbasaur.png" )
BLOCK_PIXELS = 32 #filler variable for the pixels of each square
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Player:

   """Initiates the Player"""
   #Using x,y,options(options comes from map file) as only parameters
   def __init__(self, x, y, options):
      self.x = x
      self.y = y
      self.image = player_image
      self.health = 10 #Health at 10, might change
      
   def draw(self,screen):
      screen.blit( self.image, ( self.x*32, self.y*32 ) ) 

   def update(self):
      if ( keys.press(K_LEFT) ):
         self.move( -1, 0 )
      elif ( keys.press(K_RIGHT) ):
         self.move( 1, 0 )
      elif ( keys.press(K_DOWN) ):
         self.move( 0, 1 )
      elif ( keys.press(K_UP) ):
         self.move( 0, -1 )
      if collisions.checkByType(self.x,self.y,"pit"):
         quit()

      
   def move( self, dx, dy ):
      new1 = self.x + self.image.get_width()
      new2 = self.y + self.image.get_height()
      """Check if moving will move out of bounds of the screen"""
      can_move = (new1 + dx < SCREEN_WIDTH) \
             and (new1 + dx > 0) \
             and (new2 + dy < SCREEN_HEIGHT) \
             and (new2 + dy > 0 ) \
             and (not game_engine.tilemap[self.x + dx][self.y + dy]) \
             and (not collisions.checkByType(self.x + dx, self.y + dy, "boulder"))
      if can_move:
         self.x += dx
         self.y += dy

"""
#Using main.py to test instead
clock = pygame.time.Clock()
BLOCK_PIXELS = 50 #filler variable for the pixels of each square
def keycheck():
   return pressed
pygame.init()
screen = pygame.display.set_mode((640, 480))
player = Player( 200, 200, "cat.png", screen )
# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
pygame.display.update()
screen.blit( background, (0,0 ) )

while ( True ):
   global pressed
   pressed = 0

   pos = player.image.get_rect()
   screen.blit( background, pos, pos )
   keys = pygame.key.get_pressed()
   if keys[K_LEFT]:
      pressed = K_LEFT
   elif keys[K_RIGHT]:
      pressed = K_RIGHT
   elif keys[K_UP]:
      pressed = K_UP
   elif keys[K_DOWN]:
      pressed = K_DOWN
   player.update()
   pygame.display.update()
   clock.tick( 10 )
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
      #if event.type == KEYDOWN:
       #  global pressed
        # pressed = event.key
        # player.update()
        # pygame.display.update()
"""
