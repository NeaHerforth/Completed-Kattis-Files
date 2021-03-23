#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''4 5
enter 3
enter 2
leave 1
enter 1
enter 2'''

s=s.splitlines()
firstline=s[0].split()
limit=int(firstline[0])


pot=0
denied=0
for i in range(1, len(s)):
    line=s[i].split()
    keyword=line[0]
    guests=int(line[1])
    if keyword=='enter':
        new_pot=pot +guests
        if new_pot>limit:
            denied=denied +1
        else:
            pot=new_pot
    else:
        pot=pot-guests

print(denied)

#Accepted