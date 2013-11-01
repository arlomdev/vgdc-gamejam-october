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
from player import Player
from enemy import Enemy
import collisions
from maps import Maps
from other_types import Boulder, Grass, Pit
import math
import keys

id_counter = 0
type_list = { 'player': Player,
              'grass': Grass,
              'boulder': Boulder,
              'pit': Pit,
              'enemy': Enemy
            } 
#object_list[type_name][obj_id]
object_list = {} 
mapfile = None
tilemap = []
screen = None

#Returns an "unique" ID and increments id_counter
def generate_id():
    global id_counter
    return_id = str(id_counter)
    id_counter += 1
    return return_id

def loadMap(filename):
    global mapfile
    global tilemap
    global object_list
    object_list = {}
    mapfile = Maps(filename)
    tilemap = mapfile.get_tilemap()
    for obj in mapfile.get_objectlist():
       obj_type,x,y,options = obj
       addObject(obj_type,int(x/32),int(y/32)-1,options)

def init():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.key.set_repeat(1,0)

def update():
    global object_list
    keys.update()
    for objType in object_list:
        for obj in object_list[objType]:
            object_list[objType][obj].update()

def draw():
    global screen
    global object_list
    global mapfile
    screen.fill((0,0,0))
    mapfile.draw(screen)
    for objType in object_list:
        for obj in object_list[objType]:
            object_list[objType][obj].draw(screen)
    pygame.display.flip()

def addObject(objType, x, y, optionList):
    new_id = generate_id()

    if objType not in type_list:
        return

    if objType not in object_list:
        object_list[objType] = {}

    object_list[objType][new_id] = type_list[objType](x,y,optionList)
