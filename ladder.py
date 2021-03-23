#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['1000 10']

numbers=s[0].split()

height=int(numbers[0])
angle=int(numbers[1])

import math
ladder=height/math.sin(math.radians(angle))

print(math.ceil(ladder))
#Accepted