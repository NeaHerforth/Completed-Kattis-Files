#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
3 2 3 4
10 4 4 4 4 4 4 4 4 4 4
4 10 10 10 10'''

s=s.splitlines()

#Number of  test cases
n=int(s[0])

#The rest of the lines are test cases
#Put them in lists
cases=[]
for i in range(1, len(s)):
    cases.append(s[i].split())

#Delete the first number in each test case
for i in range(len(cases)):
    del cases[i][0]

#Calculate the amount of appliances. It is one from the start without any powerstrips
for i in cases:
    appli=1
    for p in i:
        appli = appli - 1 + int(p)
    print(appli)

#Accepted
