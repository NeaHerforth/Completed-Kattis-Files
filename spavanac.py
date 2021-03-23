#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='23 40'

s=s.split()

hours=int(s[0])
minutes=int(s[1])

if minutes>=45:
    minutes=minutes-45
    print(hours, minutes)
elif hours==0:
    remains=minutes
    hours=23
    minutes=60-(45-remains)
    print(hours, minutes)
elif minutes<45:
    remains=minutes
    hours=hours -1
    minutes=60-(45-remains)
    print(hours, minutes)

#Accepted