#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''2 12 17
21
20'''

s=s.splitlines()
first_line=s[0].split()

#Amount of matches
matches=first_line[0]

#Width of box
width=int(first_line[1])

#Height of box
height=int(first_line[2])

#Max lenght across - pythagoras
import math

#The hypot() function takes the square root of x^2+y^2 - finds the hypothenuse
#Which is also the diagonal of the box
maxlenght=math.hypot(width, height)

#Find which mathes can fit in the box
for i in range(1, len(s)):
    if int(s[i])<= maxlenght:
        print('DA')
    else:
        print('NE')
#Accepted