#! /usr/bin/env python3
import sys

#n=str(sys.stdin.read())
n='3 1 5'
n=n.split()
N=n[0]
T=n[1]
M=n[2]

total= int(N)* int(T)* int(M)
print(total)

