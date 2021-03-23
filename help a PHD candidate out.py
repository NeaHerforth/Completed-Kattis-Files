#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''4
2+2
1+2
P=NP
0+0'''

s=s.splitlines()
n=int(s[0])

for i in range(1, len(s)):
    if s[i]=='P=NP':
        print('skipped')
    else:
        numbers=s[i].split('+')
        a=int(numbers[0])
        b=int(numbers[1])
        result=a+b
        print(result)
#Accepted