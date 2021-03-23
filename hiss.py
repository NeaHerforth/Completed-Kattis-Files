#! /usr/bin/env python3
import sys
#s=str(sys.stdin.read())

s='hiss'

import re

reg=re.compile('ss')
mo=reg.search(s)

if mo==None:
    print('no hiss')
else:
    print('hiss')
#Accepted