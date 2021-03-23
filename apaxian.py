#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['andrex naxos']

names=s[0].split()
first_name=names[0]
last_name=names[1]

import re
vowelreg=re.compile(r'([aeiouy]$)')
exreg=re.compile(r'ex$')

if vowelreg.search(first_name)!=None:
    first_name=vowelreg.sub(r'ex', first_name)
elif exreg.search(first_name)!=None:
    first_name=exreg.sub(r'ex', first_name)
else:
    first_name=first_name+'ex'

print(first_name+last_name)
    
#Accepted
