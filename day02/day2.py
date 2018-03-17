#!/usr/bin/env python
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()

    myInput = myInput.split('\n')
    return myInput

def part1():
    my_input = parseInput()
    amount_of_paper = 0
    for inpi in my_input:
        l, w, h = [int(x) for x in inpi.split('x')]
        area = 2 * l * w + 2 * w * h + 2 * h * l
        slack = min(l * w, w * h, h * l)
        needed_paper = area + slack
        amount_of_paper += needed_paper
    return amount_of_paper

def part2():
    my_input = parseInput()
    len_of_ribbon = 0
    for inpi in my_input:
        l, w, h = [int(x) for x in inpi.split('x')]
        wrap = 2 * (l + w + h) - 2 * max(l, w, h)
        bow = l * w * h
        len_of_ribbon += wrap + bow
    
    return len_of_ribbon
print "Part 1:", part1()
print "Part 2:", part2()