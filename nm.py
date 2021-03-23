#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3029
4
5
42
0'''

s=s.splitlines()
#All numbers in s (except 0) are numbers N

#Find sum of the numbers N and store them in a list
sumN1=[]
for i in range(0,len(s)-1):
    sum=0
    for x in s[i]:
        sum = sum + int(x)
    sumN1.append(sum)

#Find lowest number M, that is over 10, where sum(n*M) == sumN1
for x in range(0,len(s)-1):
    for p in range(11, 380000):
        multi=int(s[x])*p
        sum=0
        for i in str(multi):
            sum=sum+ int(i)
        if sum==sumN1[x]:
            print(p)
            break
#Accepted