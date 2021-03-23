#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['1 3']

tracks=s[0].split()
x_tracks=int(tracks[0])
y_tracks=int(tracks[1])

if y_tracks%2==0:
    print('possible')
else:
    print('impossible')
#Accepted