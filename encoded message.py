#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
RSTEEOTCP
eedARBtVrolsiesuAoReerles
EarSvyeqeBsuneMa'''

s=s.splitlines()

import math


square=math.sqrt(len(s[1]))
square=int(square)
matrix=[]
y=0
for i in range(square):
    line=[]
    for x in range(y,square+y):
        line.append(s[1][x])
    matrix.append(line)
    y=y+square

for x in range(1,len(matrix)+1):
    for i in range(len(matrix)**2):
        print(matrix[i][-x])

#Nope
    
        

