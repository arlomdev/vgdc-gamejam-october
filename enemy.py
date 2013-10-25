
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
