#! /usr/bin/env python3
import sys

#s=int(sys.stdin.read())

#(r1 + r2)/2 = S
#r1 + r2 =2S
#r2= 2S - r1

line='4 3'
line=line.split()
r_one=line[0]
S=line[1]

r_two= 2*int(S) - int(r_one)
print(r_two)