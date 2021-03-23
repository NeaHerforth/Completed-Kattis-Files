#! /usr/bin/env python3
import sys
#s=str(sys.stdin.read())

s='987654321'


#Find first number that is divisible by sum
for i in range(int(s), 1000000000):
    sum=0
    for x in str(i):
        sum=sum + int(x)
    if i%sum==0:
        print(i)
        break
#Accepted







