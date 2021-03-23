#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''6 40
sovl problmz
'''

s=s.splitlines()
numbers=s[0].split()

#Number of hufflepuff questions solved in total
P=numbers[-1]
print(P)

#Accepted