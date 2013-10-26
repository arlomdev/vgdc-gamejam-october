###############################################################################
#Pseudo Code layout
###############################################################################
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

###############################################################################
#Program start
###############################################################################
import pygame
from pygame.locals import *

game_engine = None;

class GameEngine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        self.typeList = {'player': '','enemy': ''} #FILL IN THE BLANKS WITH PLAYER/ENEMY OBJECTS
        self.objectList = {} #TAKES TYPE AND ID
    
    def update(self):
        for objType in self.objectList:
            for obj in self.objectList[objectType]:
                obj.update()

###############################################################################
    def addObject(objType, x, y, optionList):
        new_id = generate_id()
        
        if objType not in self.objectList:
            self.objectList[objType] = {}
        
        self.objectList[objType][new_id] = self.typeList[objType](x, y, optionList)
###############################################################################
  
def main():
    game_engine = GameEngine()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
                
        #game_engine.update()
        #game_engine.draw()

if __name__ == '__main__': main()

#Returns an "unique" ID and increments id_counter
id_counter = 0

def generate_id():
    global id_counter
    return_id = id_counter.str()
    id_counter += 1
    return return_id
    
    
    
