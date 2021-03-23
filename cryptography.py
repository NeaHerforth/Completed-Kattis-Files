#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['SECRET']

word=s[0]

count=0
for i in range(len(word)):
    if i%3==0 and word[i]=='P':
        continue
    elif i%3==1 and word[i]=='E':
        continue
    elif i%3==2 and word[i]=='R':
        continue
    else:
        count+=1
print(count)
#Accepted