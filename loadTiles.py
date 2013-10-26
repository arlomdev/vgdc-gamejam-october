import pygame
import pygame.locals
import json

class Map:

  pixelw = 32
  pixelh = 32

  json_input = open("maps/introLevel.json").read()

  data = json.loads(json_input)
  # test print data['layers'][0]['data']

  # store tile data into map_lo
  def getWall():
    height = data['layers'][0]['height']
    width= data['layers'][0]['width']
    map_lo = [[0 for j in range(width)] for i in range(height)]
    n = 0
    for row in map_lo:
      for tile in range(len(row)):
        row[tile] = data['layers'][0]['data'][n]
        n += 1

  # prints out the map layout
  for row in map_lo:
    for tile in row:
      print tile, " ",
    print "\n"


  def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width/width):
      line = []
      tile_table.append(line)
      for tile_y in range(0, image_height/height):
        rect = (tile_x*width, tile_y*height, width, height)
        line.append(image.subsurface(rect))
    return tile_table

#  if __name__=='__main__':
#    pygame.init()
#    screen = pygame.display.set_mode((640, 480))
#    screen.fill((255, 255, 255))
#    table = load_tile_table(filename, w, h)
#    for x, row in enumerate(table):
#      for y, tile in enumerate(row):
#        screen.blit(tile, (x*32, y*32))
#    pygame.display.flip()
#    while pygame.event.wait().type != pygame.locals.QUIT:
#      pass

