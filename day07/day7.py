#!/usr/bin/env python
import sys
import collections

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def printDict(myDict):
  od = collections.OrderedDict(sorted(myDict.items()))
  for key, val in od.items():
    st = key + ": "
    if val < 0:
      st += str(2 ** 16 + val)
    else:
      st += str(val)
    if key == "a":
      print st
      return

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def evaluateWires(overrideWire = None, overrideValue = 0):
  inp = parseInput()
  queue = []
  for line in inp:
    queue.append(line)
  valu_dict = {}
  while queue:
    line = queue.pop(0)
    spl = line.split(' -> ')
    target = spl[-1]
    operator = spl[0].split(' ')
    numArgs = len(operator)

    if numArgs == 1:
      if overrideWire == target:
        valu_dict[target] = overrideValue
      elif is_number(operator[0]):
        val = int(operator[0])
        valu_dict[target] = val
      elif operator[0] in valu_dict:
        valu_dict[target] = valu_dict[operator[0]]
      else:
        queue.append(line)

    elif numArgs == 2:
      if is_number(operator[1]):
        val = int(operator[0])
        valu_dict[target] = ~val
      elif operator[1] in valu_dict:
        valu_dict[target] = ~valu_dict[operator[1]]
      else:
        queue.append(line)
    
    elif numArgs == 3:
      op0 = operator[0]
      op2 = operator[2]

      if op0 in valu_dict:
        op0 = valu_dict[op0]
      elif is_number(op0):
        op0 = int(op0)
      else:
        queue.append(line)
        continue
      op2 = operator[2]
      if op2 in valu_dict:
        op2 = valu_dict[op2]
      elif is_number(op2):
        op2 = int(op2)
      else:
        queue.append(line)
        continue 

      if operator[1] == "AND":
        valu_dict[target] = op0 & op2
      elif operator[1] == "OR":
        valu_dict[target] = op0 | op2
      elif operator[1] == "RSHIFT":
        valu_dict[target] = op0 >> op2
      elif operator[1] == "LSHIFT":
        valu_dict[target] = op0 << op2
  printDict(valu_dict)


def part1():
  evaluateWires()

def part2():
  evaluateWires(overrideWire="b", overrideValue=956)

part1()
part2()