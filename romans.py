#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['20.267']

engM=float(s[0])

x= 1000*(5280/4854)

paces=(engM*x)
paces=round(paces)
print(paces)

#Accepted