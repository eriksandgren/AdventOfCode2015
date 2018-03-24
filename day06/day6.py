#!/usr/bin/env python
import operator

class Grid2D():
  def __init__(self, size):
    self.grid = [[0] * size for _ in range(size)]
    self.size = size
  def display(self):
    print
    for l in self.grid:
      print l
  
  def mark(self, x, y):
    self.grid[y][x] = 1

  def unmark(self, x, y):
    self.grid[y][x] = 0

  def toggle(self, x, y):
    if self.grid[y][x] == 1:
      self.grid[y][x] = 0
    else:
      self.grid[y][x] = 1

  def up(self, x, y):
    self.grid[y][x] += 1

  def down(self, x, y):
    if self.grid[y][x] >= 1:
      self.grid[y][x] -= 1

  def numMarked(self):
    marked = 0
    for x in xrange(self.size):
      for y in xrange(self.size):
        if self.grid[y][x] == 1:
          marked += 1
    return marked
  
  def totalBrightness(self):
    brightness = 0
    for x in xrange(self.size):
      for y in xrange(self.size):
        brightness += self.grid[y][x]
    return brightness

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    myInput = myInput.split('\n')
    return myInput

def redistribute(state):
  index, blocksToDistribute = max(enumerate(state), key=operator.itemgetter(1))
  state[index] = 0
  numBlocks = len(state)
  while blocksToDistribute != 0:
    index = (index + 1) % (numBlocks)
    blocksToDistribute -= 1
    state[index] += 1    
  
  return state

def part1():
  inp = parseInput()
  grid = Grid2D(1001)
  for cmd in inp:
    cmd = cmd.replace(',', ' ')
    indexes = [int(s) for s in cmd.split() if s.isdigit()]
    for x in xrange(indexes[0], indexes[2] + 1):
      for y in xrange(indexes[1], indexes[3] + 1):
        if 'toggle' in cmd:
          grid.toggle(x,y)
        elif 'off' in cmd:
          grid.unmark(x,y)
        else:
          grid.mark(x,y)
  print grid.numMarked()
  
def part2():
  inp = parseInput()
  grid = Grid2D(1001)
  for cmd in inp:
    cmd = cmd.replace(',', ' ')
    indexes = [int(s) for s in cmd.split() if s.isdigit()]
    for x in xrange(indexes[0], indexes[2] + 1):
      for y in xrange(indexes[1], indexes[3] + 1):
        if 'toggle' in cmd:
          grid.up(x,y)
          grid.up(x,y)
        elif 'off' in cmd:
          grid.down(x,y)
        else:
          grid.up(x,y)
  print grid.totalBrightness()   
      
  
part1()
part2()
