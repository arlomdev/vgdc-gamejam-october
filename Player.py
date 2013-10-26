import pygame, sys
from pygame.locals import *

class Player:

   """Initiates the Player"""
   def __init__(self, x, y, image, screen):
      self.x = x
      self.y = y
      self.image = pygame.image.load( image )
      self.health = 10 #Health at 10, might change
      self.screen = screen
      self.draw()
      
   def draw(self):
      self.screen.blit( self.image, ( self.x, self.y ) ) 

   def update(self):
      key = keycheck()
      if ( key == K_LEFT ):
         self.move( -BLOCK_PIXELS, 0 )
      elif ( key == K_RIGHT ):
         self.move( BLOCK_PIXELS, 0 )
      elif ( key == K_DOWN ):
         self.move( 0, BLOCK_PIXELS )
      elif ( key == K_UP ):
         self.move( 0, -BLOCK_PIXELS )

      
   def move( self, xDelta, yDelta ):
      new1 = self.x + self.image.get_width()
      new2 = self.y + self.image.get_height()
      """Check if moving will move out of bounds of the screen"""
      if ( new1 + xDelta < self.screen.get_width() and new1 + 
         xDelta > 0 and new2 + yDelta < self.screen.get_height() and
         new2 + yDelta > 0 ):
         self.x += xDelta
         self.y += yDelta
         self.screen.blit( self.image, ( self.x, self.y ) )

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
