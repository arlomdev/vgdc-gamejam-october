import pygame

BOULDER_IMAGE = pygame.image.load("img/Boulder.png")
PIT_IMAGE = pygame.image.load("img/pit.png").convert().subsurface(128,32,32,32)
GRASS_IMAGE = pygame.image.load("img/Grass.png")

class Boulder:
    def __init__(self,x,y,options):
        self.x = x
        self.y = y
        self.obj_type = "boulder"
        self.image = BOULDER_IMAGE

    def update(self):
        return None

    def draw(self,screen):
        screen.blit(self.image,self.x,self.y)

class Grass:
    def __init__(self,x,y,options):
        self.x = x
        self.y = y
        self.obj_type = "grass"
        self.image = GRASS_IMAGE

    def update(self):
        return None

    def draw(self,screen):
        screen.blit(self.image,self.x,self.y)

class Pit:
    def __init__(self,x,y,options):
        self.x = x
        self.y = y
        self.obj_type = "pit"
        self.image = PIT_IMAGE

    def update(self):
        return None

    def draw(self,screen):
        screen.blit(self.image,self.x,self.y)
