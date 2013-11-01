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
import game_engine

def main():
    game_engine.init()
    game_engine.loadMap("maps/level2.json")
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        game_engine.update()
        game_engine.draw()

if __name__ == '__main__': main()
