#!/usr/bin/env python
import sys
import md5

def parseInput():
    file = open("input.txt")
    return file.readline()[:]

def part1():
    my_input = parseInput()
    tick = 1
    notFound = True
    while notFound:
      currentStr = my_input + str(tick)
      m = md5.new()
      m.update(currentStr)
      retStr = m.hexdigest()
      if retStr[0:5] == '00000':
        notFound = False
        print retStr
        print tick
      tick += 1
  
    


def part2():
    my_input = parseInput()
    tick = 1
    notFound = True
    while notFound:
      currentStr = my_input + str(tick)
      m = md5.new()
      m.update(currentStr)
      retStr = m.hexdigest()
      if retStr[0:6] == '000000':
        notFound = False
        print retStr
        print tick
      tick += 1

part1()
part2()