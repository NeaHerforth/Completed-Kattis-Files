#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()


s='''3
Raise your right hand.
Lower your right hand.
Simon says raise your left hand.'''

s=s.splitlines()
lines=int(s[0])

#Create regex object to find sentences that start with 'Simon says' and ends with some words
import re
simonReg=re.compile(r'(Simon says) (.*)')



for i in range(1, len(s)):
    sentence=s[i]
    mo=simonReg.search(sentence)
    if mo==None:
        continue
    else: 
        print(mo.group(2))

#Accepted
