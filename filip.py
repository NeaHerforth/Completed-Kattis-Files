#! /usr/bin/env python3
import sys
#s=str(sys.stdin.read())

s='839 237'
s=s.split()

A=s[0]
B=s[1]

#find reverse number of A
revA=[]
for i in range(2,-1,-1):
    revA.append(str(A[i]))

newA=''.join(revA)

#find reverse number of B
revB=[]
for i in range(2,-1,-1):
    revB.append(str(B[i]))

newB=''.join(revB)

#compare the two reversed numbers

if newA > newB:
    print(newA)
else:
    print(newB)

#Accepted