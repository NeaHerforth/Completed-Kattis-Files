#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['4 2 1']
meassures=s[0].split()

sides=int(meassures[0])
h=int(meassures[1])
v=int(meassures[2])

height=4

piece1=h*v*height
piece2=(sides-h)*v*height
piece3=(sides-v)*h*height
piece4=(sides-h)*(sides-v)*height

volumes=[]
volumes.append(piece1)
volumes.append(piece2)
volumes.append(piece3)
volumes.append(piece4)

print(max(volumes))