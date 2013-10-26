def lookout_ai(self):
    player = [p for p in game_engine.objectList["player"]][0]
    x = self.x
    y = self.y
    if player.x == self.x:
        dy = player.y - self.y
        for i in range(0,math.abs(dy)+1):
            if dy > 0:
                y = self.y + i
            else:
                y = self.y - i
            if game_engine.tilemap[self.x][y] or collision.checkPos(self.x,y,"grass"):
                break
            if collision.checkPos(self.x,y,"player"):
                #game over buddy
    if player.y == self.y:
        dx = player.x - self.x
        for i in range(0,math.abs(dx)+1):
            if dx > 0:
                x = self.x + i
            else:
                x = self.x - i
            if game_engine.tilemap[x][self.y] or collision.checkPos(x,self.y,"grass"):
                break
            if collision.checkPos(x,self.y,"player"):
                #game over buddy

def pacer_ai(self):
    if self.facing == "right":
        move(1,0)
    if self.facing == "left":
        move(-1,0)
    if self.facing == "up":
        move(0,-1)
    if self.facing == "down":
        move(0,1)
    lookout_ai(self)

class Enemy:
    def __init__(self,gid,x,y,options):
        self.gid = gid
        self.x = x
        self.y = y
        self.ai = ai_list[options.ai_type]
        self.facing = options.facing

    def update(self):
        self.ai(self)
    
    def draw(self):
        drawImage(enemy_sprite,self.x*32, self.y*32)
