#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
10
9
-5'''

s=s.splitlines()

for i in range(1, len(s)):
    if int(s[i])%2==0:
        print(str(s[i])+ ' is even')
    else:
        print(str(s[i])+ ' is odd')

#accepted