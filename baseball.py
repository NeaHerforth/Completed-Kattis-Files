#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
3 0 2
'''

s=s.splitlines()

#Total number of hits
bats=float(s[0])

#The points per hit in a list
bases=s[1].split()

newbase=[]
count=0
for i in range(len(bases)):
    if bases[i]=='-1':
        count +=1
    else:
        newbase.append(bases[i])

sumBases=0
for i in newbase:
    sumBases=sumBases + int(i)

#Find slugging percentage 
slugging=sumBases/(bats-count)
print(slugging)

#Accepted