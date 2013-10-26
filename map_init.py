import pygame
import pygame.locals
import json

json_input = open("maps/introLevel.json").read()

data = json.loads(json_input)
# print data['layers'][0]['data']

height = data['layers'][0]['height']
width= data['layers'][0]['width']
row_lo = [0 for i in range(width)]
map_lo = [[0 for j in range(len(row_lo))] for i in range(height)]

n = 0
m = 0

print len(map_lo)

for a in range(0, height):
  # print a, "HERE"
  for b in range(0, width):
    row_lo[b] = data['layers'][0]['data'][n]
    #print row_lo[b]
    n += 1
  map_lo[a] = row_lo
  print map_lo[a]

#for a in map_lo:
#  for b in map_lo[b]:
#    print b
#    print map_lo[a][b],
#  print "\n"

# for x, row in range(0, 3):
#  print "blah"
