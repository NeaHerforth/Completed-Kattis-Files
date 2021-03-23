#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''39
40
41
42
43
44
82
83
84
85'''

s=s.splitlines()

remainders=[]
for i in s:
    mod=int(i)%42
    remainders.append(mod)

count={}
for i in remainders:
    count.setdefault(i, 0)
    count[i]=count[i]+1

#Print out only the len of keys in count
distinct=len(count.keys())
print(distinct)