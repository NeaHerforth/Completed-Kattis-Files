#! /usr/bin/env python3
import sys

s=str(sys.stdin.read())

count=0
for i in s:
    if i=='e':
        count +=1

hey='h' + 'e'*count*2 +'y'
print(hey)

#Accepted