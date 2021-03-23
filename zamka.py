#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''1
10000
1'''
s=s.splitlines()

#N is the lowest number between L and  D - sum is X
#M is the biggest number between L and  D - sum is X

L=int(s[0])
D=int(s[1])
X=int(s[2])

#Find N 
numbers=[]
for i in range(L, D+1):
    i=str(i)
    count=0
    for num in i:
        count=count+int(num)
    if count==X:
        numbers.append(i)
print(numbers[0])
print(numbers[-1])

#Accepted