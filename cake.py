#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''4
7
2 3
1 4
1 2
1 2
2 2
2 2
2 1'''

s=s.splitlines()
print(s)

#width of the cake
W=int(s[0])

#number of shattered pieces of cake
N=int(s[1])

#Calculate area because W*L=area so, L=area/W
totalArea=0
for i in range(2, N+2):
    area=int(s[i][0])*int(s[i][-1])
    totalArea= totalArea + area

#L=area/W
lenght=totalArea/W
print(int(lenght))