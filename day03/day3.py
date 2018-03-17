#!/usr/bin/env python
import sys
class Grid2D():
  def __init__(self, size):
    self.grid = [["O"] * size for _ in range(size)]
    self.x = int(size / 2)
    self.y = int(size / 2)
    self.x_init = self.x
    self.y_init = self.y
    self.mark()

  def display(self):
    print
    for l in self.grid:
      print l
  
  def mark(self):
    self.grid[self.y][self.x] = 'x'

  def visited(self):
    return self.grid[self.y][self.x] == 'x'

  def move(self, x_delta, y_delta):
    self.x = self.x + x_delta
    self.y = self.y + y_delta

  def moveUp(self):
    self.move(0, -1)

  def moveDown(self):
    self.move(0, 1)

  def moveRight(self):
    self.move(1, 0)

  def moveLeft(self):
    self.move(-1, 0)

  def resetPosition(self):
    self.x = self.x_init
    self.y = self.y_init

def parseInput():
    file = open("input.txt")
    return file.readline()[:]

def part1():
    my_input = parseInput()
    grid = Grid2D(1001)
    num_visisted = 1
    for c in my_input:
      if c == '<':
        grid.moveLeft()
      elif c == '>':
        grid.moveRight()
      elif c == '^':
        grid.moveUp()
      elif c == 'v':
        grid.moveDown()
      
      if not grid.visited():
        num_visisted += 1
        grid.mark()
    print num_visisted



def part2():
    my_input = parseInput()
    grid = Grid2D(1001)
    num_visisted = 1
    santa = my_input[0::2]
    robo = my_input[1::2]
    for instructions in [santa, robo]:
      grid.resetPosition()
      for c in instructions:
        if c == '<':
          grid.moveLeft()
        elif c == '>':
          grid.moveRight()
        elif c == '^':
          grid.moveUp()
        elif c == 'v':
          grid.moveDown()
        
        if not grid.visited():
          num_visisted += 1
          grid.mark()
    print num_visisted

part1()
part2()