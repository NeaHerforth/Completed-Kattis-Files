#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''30 20
10 10
10 20'''

s=s.splitlines()

min_x=1000
min_y=1000
max_x=0
max_y=0

all_lines=[]
for i in range(len(s)):
    line=s[i].split()
    x=int(line[0])
    y=int(line[1])
    int_line=[x,y]
    all_lines.append(int_line)
    if x<min_x:
        min_x=x
    if x>max_x:
        max_x=x
    if y<min_y:
        min_y=y
    if y>max_y:
        max_y=y

min_max=[min_x, max_y]
max_max=[max_x, max_y]
max_min=[max_x, min_y]
min_min=[min_x, min_y]


if min_max not in all_lines:
    print(min_max[0], min_max[1])
elif max_max not in all_lines:
    print(max_max[0], max_max[1])
elif max_min not in all_lines:
    print(max_min[0], max_min[1])
else:
    print(min_min[0], min_min[1])


