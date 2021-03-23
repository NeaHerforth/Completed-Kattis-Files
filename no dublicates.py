#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['THE RAIN IN SPAIN']

words=s[0].split()


count={}
for i in words:
    count.setdefault(i, 0)
    count[i]=count[i]+1

stat=0
for v in count.values():
    if int(v)>1:
        print('no')
        break
    else:
        stat= stat +1
if stat==len(words):
    print('yes')
#Accepted