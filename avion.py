#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''N-FBI1
9A-USKOK
I-NTERPOL
G-MI6
RF-KGB1'''

s=s.splitlines()

#Create regex object to find the string 'FBI'
import re
fbireg=re.compile('FBI')

indexes=[]
for i in range(len(s)):
    if fbireg.search(s[i])!=None:
        indexes.append(i+1)

if indexes==[]:
    print('HE GOT AWAY!')
else:
    for i in indexes:
        print(i, end=' ')