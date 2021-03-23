
#! /usr/bin/env python3
import sys

#work= '1;3;5;8;13'
work=str(sys.stdin.read())

work=work.split(';')

import re

#Create regex objects to look for hyphen, first digit before hyphen, and last digit after hyphen
lineReg=re.compile(r'-')
firstDigReg=re.compile(r'^\d*')
lastDigReg=re.compile(r'\d*$')

new=[]

for i in range(len(work)):
    mo=lineReg.search(work[i])
    if mo!= None:
        first=firstDigReg.search(work[i]).group()
        last=lastDigReg.search(work[i]).group()
        for x in range(int(first), int(last)+1):
            new.append(x)
    else:
        new.append(int(work[i]))

new.sort()
print(len(new))

#accepted
