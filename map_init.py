import pygame
import pygame.locals
import json

json_input = open("maps/introLevel.json").read()

data = json.loads(json_input)
# print data['layers'][0]['data']

height = data['layers'][0]['height']
width= data['layers'][0]['width']
map_lo = [[0 for j in range(width)] for i in range(height)]

n = 0

# store tile data into map_lo
#for i in range(height):
 # for j in range(width):
  #  map_lo[i][j] = data['layers'][0]['data'][n]
   # n += 1

for row in map_lo:
  for tile in range(len(row)):
     row[tile] = data['layers'][0]['data'][n]
     n += 1

# prints out the map layout
for row in map_lo:
  for tile in row:
    print tile, " ",
  print "\n"

