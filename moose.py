#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['0 0']
tines=s[0].split()

left=int(tines[0])
right=int(tines[1])

if left>right:
    max_number=left
elif left==right:
    max_number=left
else:
    max_number=right

number=max_number*2

if left==0 and right==0:
    print('Not a moose')
elif left==right:
    stat='Even'
    print(stat, number)
else:
    stat='Odd'
    print(stat, number)

#Accepted