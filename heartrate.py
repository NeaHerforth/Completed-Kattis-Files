#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''2
6 5.0000
2 3.1222'''

s=s.splitlines()

#Number of cases
n=int(s[0])

#BPM --> 60b/p
for i in range(1, n+1):
    case= s[i].split()
    b=float(case[0])
    p=float(case[1])
    #Calculate BPM
    bpm=(60*b)/p
    #Variance (ABPM)
    var=60/p
    print(bpm-var, bpm, bpm+var)

#Accepted