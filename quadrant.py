#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''9
-13'''
s=s.splitlines()

x=int(s[0])
y=int(s[1])

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)

#Accepted