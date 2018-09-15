#!/usr/bin/env python
import sys
import re

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def countCharsDecode(s):
  strLen = len(s)
  
  s = s[1:-1]
  s = re.sub('\\\\\\\\', '_', s)
  s = re.sub('\\\\x..', ' ', s)
  s = re.sub('\\\\.', '+', s)
  memLen = len(s)

  return strLen - memLen

def countCharsEncode(s):
  strLen = len(s)
  print s
  s = re.sub('\\\\', '\\\\\\\\', s)
  s = re.sub('\\"', '\\\\"', s)
  s =  "\"" + s + "\""
  print s
  memLen = len(s)

  return memLen - strLen 

def part1():
  inp = parseInput()
  tot = 0
  for string in inp:
    tot += countCharsDecode(string)
  print tot

def part2():
  inp = parseInput()
  tot = 0
  for string in inp:
    tot += countCharsEncode(string)
  print tot

part1()
part2()