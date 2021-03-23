#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''10
-100 40000 -6500 -230 -18 34500 -450 13000 -100 5000'''
s=s.splitlines()

n=int(s[0])

in_out=s[1].split()

exp=[]
for i in in_out:
    if int(i)<0:
        exp.append(int(i))

#Calculate the sum of the expenses
all_exp=0
for i in exp:
    all_exp=all_exp + abs(i)
print(all_exp)
#Accepted