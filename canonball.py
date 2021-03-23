#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''11
19 45 20 9 12
20 45 20 9 12
25 45 20 9 12
20 43 20 9 12
20 47.5 20 9 12
20 45 17 9 12
20 45 24 9 12
20 45 20 10 12
20 45 20 9 11
20 45 20 9.0 11.5
20 45 18.1 9 12'''

s=s.splitlines()

#Number of cases
n=int(s[0])

import math
g=9.81
for i in range(1, len(s)):
    line=s[i].split()
    #Define parameters
    velocity=float(line[0])
    angle=float(line[1])
    x_distance=float(line[2])
    lower_wall=float(line[3])
    upper_wall=float(line[4])
    #Calculate 
    time=x_distance/velocity/math.cos(math.radians(angle))   #To us the cos function, you have to convert to radians
    y=(velocity*time*math.sin(math.radians(angle)))-(0.5*g*time*time)
    if y-lower_wall>=1 and upper_wall - y>= 1:
        print('Safe')
    else:
        print('Not Safe')
#Accepted

