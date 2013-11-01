import game_engine
import collisions
import pygame

def lookout_ai(self):
    player = [game_engine.object_list["player"][pid] for pid in game_engine.object_list["player"]][0]
    x = self.x
    y = self.y
    if player.x == self.x:
        dy = player.y - self.y
        for i in range(0,abs(dy)+1):
            if dy > 0:
                y = self.y + i
            else:
                y = self.y - i
            if game_engine.tilemap[self.x][y] or collisions.checkByType(self.x,y,"grass"):
                break
            #if collision.checkByType(self.x,y,"player"):
                #game over buddy
    if player.y == self.y:
        dx = player.x - self.x
        for i in range(0,abs(dx)+1):
            if dx > 0:
                x = self.x + i
            else:
                x = self.x - i
            if game_engine.tilemap[x][self.y] or collisions.checkByType(x,self.y,"grass"):
                break
            #if collision.checkByType(x,self.y,"player"):
                #game over buddy

def pacer_ai(self):
    if self.facing == "right":
        self.move(1,0)
    if self.facing == "left":
        self.move(-1,0)
    if self.facing == "up":
        self.move(0,-1)
    if self.facing == "down":
        self.move(0,1)
    lookout_ai(self)

ai_list = {
    "lookout" : lookout_ai,
    "pacer" : pacer_ai
}

ENEMY_IMAGE = pygame.image.load("img/Rocket.png")

class Enemy:
    def __init__(self,x,y,options):
        self.x = x
        self.y = y
        self.image = ENEMY_IMAGE
        if options:
            self.ai = ai_list[options["ai_type"]]
            self.facing = options["facing"]
        else:
            self.facing = "up"
            self.ai = lookout_ai

    def update(self):
        self.ai(self)
    
    def draw(self,screen):
        screen.blit(self.image,(self.x*32, self.y*32))
      
    def move( self, dx, dy ):
      new1 = self.x + self.image.get_width()
      new2 = self.y + self.image.get_height()
      """Check if moving will move out of bounds of the screen"""
      can_move = (not game_engine.tilemap[self.x + dx][self.y + dy]) \
             and (not collisions.checkByType(self.x + dx, self.y + dy, "boulder"))
      if can_move:
         self.x += dx
         self.y += dy
