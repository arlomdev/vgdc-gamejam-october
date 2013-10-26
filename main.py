#load tile map

#generate ID
# use a id_counter to make sure each id is unique

#GameEngine Class

# update
# for all the objects in the game call their update function

# draw
# for all the objects in the game call their draw function

# GameObject
# Template object for creating objects
# needs an up

import pygame
from pygame.locals import *

game_engine = None;

class GameEngine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        self.typeList = {}
        
        self.objectList = {}
    
    def update(self):
        for type in self.objectList:
            for object in self.objectList[type]:
                object.update()
    
 
#clear screen at begining of function, and flip at end
def main():
    game_engine = GameEngine()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
                
        #game_engine.update()
        #game_engine.draw()
  
if __name__ == '__main__': main()

