#!/usr/bin/env python
import sys

bannedStrings = ["ab", "cd", "pq", "xy"]
def containsBanned(inpStr):
  for s in bannedStrings:
    if s in inpStr:
      return True
  return False

def containsRepetition(inpStr):
  stringLen = len(inpStr)
  for s1,s2 in zip(inpStr[0:-1], inpStr[1:]):
    if s1 == s2:
      return True
  return False

vowels = "aeiou"
def containsVowels(inpStr):
  vowelCnt = 0
  for c in inpStr:
    if c in vowels:
      vowelCnt += 1
      if vowelCnt == 3:
        return True
  return False

def containsRepetition2(inpStr):
  stringLen = len(inpStr)
  for i in xrange(0, stringLen - 1):
    myStr = inpStr[i : i + 2]
    if myStr in inpStr[:i] or myStr in inpStr[i + 2 :]:
      return True
  return False

def containsRepetition3(inpStr):
  stringLen = len(inpStr)
  for s1, s2 in zip(inpStr[0:-2], inpStr[2:]):
    if s1 == s2:
      return True
  return False

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput
def part1():
    my_input = parseInput()
    niceCount = 0
    for w in my_input:
      if not containsBanned(w) and containsRepetition(w) and containsVowels(w):
        niceCount += 1
    print niceCount

def part2():
    my_input = parseInput()
    niceCount = 0
    for w in my_input:
      if containsRepetition2(w) and containsRepetition3(w):
        niceCount += 1
    print niceCount


part1()
part2()