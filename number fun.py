#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''6
1 2 3
2 24 12
5 3 1
9 16 7
7 2 14
12 4 2'''

s=s.splitlines()

#number of cases
n=int(s[0])

cases=[]
for i in range(1, len(s)):
    case=s[i].split()
    cases.append(case)

for i in cases:
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    if a+b==c :
        print('Possible')
    elif a-b==c or b-a==c:
        print('Possible')
    elif a*b==c or b*a==c:
        print('Possible')
    elif a/b==c or b/a==c:
        print('Possible')
    else:
        print('Impossible')


