#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''0.75
2
2 3.333
3.41 4.567'''

s=s.splitlines()

#Cost of seed to plant one square meter
cost=float(s[0])

#Number oflawns to sow
lawns=float(s[1])

lawnSizes=[]
for i in range(2, len(s)):
    lawnSizes.append(s[i].split())

#Find size of lawns and add them together
totalArea=0
for i in lawnSizes:
    area=float(i[0])*float(i[1])
    totalArea=totalArea + area

#Multiply the total area with the price pr. square meter
price=totalArea*cost
print(price)

#Accepted