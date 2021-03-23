#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''5
-14 -5 -39 -5 -7'''

s=s.splitlines()

#Number of temperatures collected
n=int(s[0])

#Temperatures
temp=s[1].split()

#Find out how many temps are below 0 degrees
count=0
for i in temp:
    if int(i)<0:
        count +=1
print(count)

#Accepted
