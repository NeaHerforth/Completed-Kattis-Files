#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''5 5
motor
hull
left_oar
hulle
motore'''

s=s.splitlines()

first_line=s[0].split()
parts=int(first_line[0])
days=int(first_line[1])

count={}
stat=''
for i in range(1, len(s)):
    if len(count.keys())==parts:
        stat='done'
        print(i-1)
        break
    else:
        count.setdefault(s[i], 0)
        count[s[i]]=count[s[i]] +1

if len(count.keys())==parts and stat !='done':
    print(days)
elif len(count.keys())<parts:
    print('paradox avoided')
#Accepted
