import pygame
from pygame.locals import *

key_dict = {}

"""
def update(event):
    if event.type == KEYDOWN or event.type == KEYUP:
        if event.key not in key_dict:
            key_dict[event.key] = (False,False)
    if event.type == KEYDOWN:
        key_dict[event.key] = (True, key_dict[event.key][0])
    elif event.type == KEYUP:
        key_dict[event.key] = (False, False)
"""
def update():
    keys = pygame.key.get_pressed()
    for key, value in enumerate(keys):
        if key not in key_dict:
            key_dict[key] = (False, False)
        key_dict[key] = (value, key_dict[key][0])

def check(key_code):
    if key_code in key_dict:
        return key_dict[key_code]
    else:
        return (False, False)

def down(key_code):
    return check(key_code)[0]

def up(key_code):
    return (not down(key_code))

def repeated(key_code):
    crnt, prev = check(key_code) 
    return (crnt and prev)

def press(key_code):
    crnt, prev = check(key_code) 
    return (crnt and (not prev))
