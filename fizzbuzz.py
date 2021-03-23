#! /usr/bin/env python3
import sys
#s=str(sys.stdin.read())

s='3 5 7'
s=s.split()

X=int(s[0])
Y=int(s[1])
N=int(s[2])

for i in range(1, N+1):
    if i%X==0 and i%Y==0:
        print('FizzBuzz')
    elif i%X==0:
        print('Fizz')
    elif i%Y==0:
        print('Buzz')
    else:
        print(i)