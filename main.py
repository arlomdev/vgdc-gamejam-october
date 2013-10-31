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
from Player import Player
#from enemy import Enemy
import collisions
from Maps import Maps
from other_types import Boulder, Grass, Pit
import math
import keys

game_engine = None

#Returns an "unique" ID and increments id_counter
id_counter = 0

def generate_id():
    global id_counter
    return_id = str(id_counter)
    id_counter += 1
    return return_id

class GameEngine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        pygame.key.set_repeat(1,0)
        self.typeList = {'player': Player,
                         'grass': Grass,
                         'boulder': Boulder,
                         'pit': Pit
                        } 
        self.objectList = {} #TAKES TYPE AND ID
        self.mapfile = Maps("maps/testLevel.json")
        self.tilemap = self.mapfile.get_tilemap()
        for obj in self.mapfile.get_objectlist():
           obj_type,x,y,options = obj
           self.addObject(obj_type,int(x/32),int(y/32),options)

    def update(self):
        keys.update()
        for objType in self.objectList:
            for obj in self.objectList[objType]:
                self.objectList[objType][obj].update(self)

    def draw(self):
        self.screen.fill((0,0,0))
        self.mapfile.draw(self.screen)
        for objType in self.objectList:
            for obj in self.objectList[objType]:
                self.objectList[objType][obj].draw(self.screen)
        pygame.display.flip()
###############################################################################
    def addObject(self,objType, x, y, optionList):
        new_id = generate_id()

        if objType not in self.objectList:
            self.objectList[objType] = {}

        self.objectList[objType][new_id] = self.typeList[objType](x,y,optionList)
###############################################################################

def main():
    game_engine = GameEngine()
    # game_engine.addObject("player",100,100,{})
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            #else:
            #    keys.update(event)
        game_engine.update()
        game_engine.draw()

if __name__ == '__main__': main()
