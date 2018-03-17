#!/usr/bin/env python
import sys

def parseInput():
    file = open("input.txt")
    return file.readline()[:]

def part1():
    my_input = parseInput()
    opening = my_input.count('(')
    closing = my_input.count(')')
    floor = opening - closing
    return floor

def part2():
    my_input = parseInput()
    floor = 0
    instruction = 0
    for c in my_input:
        instruction += 1
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1:
            return instruction

print "Part 1:", part1()
print "Part 2:", part2()