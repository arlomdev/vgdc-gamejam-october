import pygame
import pygame.locals
import json

pixelw = 32
pixelh = 32
# test print data['layers'][0]['data']

class Maps:

  def __init__(self, Filename):
    json_input = open(Filename).read()
    self.data = json.loads(json_input)
    self.img = pygame.image.load("img/Tiles Set.png").convert()

  # store tile data into map_lo
  def get_tilemap(self):
    height = self.data['layers'][0]['height']
    width = self.data['layers'][0]['width']
    map_lo = [[0 for j in range(height)] for i in range(width)]
    n = 0
    m = 0
    for row in map_lo:
      for tile in range(len(row)):
        row[tile] = self.data['layers'][0]['data'][n + m]
        m += width
      n += 1
      m = 0
    # replace map_lo w/ 1's and 0's
    wall = map_lo[0][0]
    for row in map_lo:
      for tile in range(len(row)):
        if (row[tile] == wall):
          row[tile] = 1
        else:
          row[tile] = 0
    return map_lo


  # get the list of containers (objects)
  def get_objectlist(self):
    obj_list = []
    for layer in self.data['layers']:
      if (layer['type'] == "tilelayer"):
        continue
      else:
        name = layer['name']
        for obj in layer['objects']:
          obj_list.append((name, obj['x'], obj['y'], obj['properties']))
    return obj_list


  # Draws background
  def draw(self, screen):
    floorRect = ( 0, 0, pixelw, pixelh)
    wallRect = ( 96, 32, pixelw, pixelh)
    wallImg = (self.img).subsurface(wallRect)
    floorImg = (self.img).subsurface(floorRect)
    wallMap = self.get_tilemap()
    tile_table = []
    for tile_x in range(len(wallMap)):
      line = []
      tile_table.append(line)
      for tile_y in range(len(wallMap[0])):
        # fill w/ wall or floor
        if (wallMap[tile_x][tile_y] == 0):
          line.append(floorImg)
        else:
          line.append(wallImg)
    # draw on screen
    for x, row in enumerate(tile_table):
      for y, tile in enumerate(row):
        screen.blit(tile, (x*32, y*32))

# test functions with main
#if __name__=='__main__':
#
#  # prints out the map layout
#  wallMap = getWall()
#  for row in wallMap:
#    for tile in row:
#      print tile, " ",
#    print "\n"
#
#  pygame.init()
#  screen = pygame.display.set_mode((640, 480))
#  screen.fill((255, 255, 255))
#
#  wallFile = "samwall.png"
#  floorFile = "samfloor.png"
#
#  table = load_tile_table(wallMap, wallFile, floorFile)
#  for x, row in enumerate(table):
#    for y, tile in enumerate(row):
#      screen.blit(tile, (x*32, y*32))
#  pygame.display.flip()
#  while pygame.event.wait().type != pygame.locals.QUIT:
#    pass

