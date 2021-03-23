#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
ATCCGCTTAGAGGGATT
GTCCGTTTAGAAGGTTT
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
abcdefghijklmnopqrstuvwxyz0123456789
abcdefghijklmnopqrstuvwxyz0123456789'''

s=s.splitlines()

all_cases=[]
i=1
while i<len(s):
    case=[]
    case.append(s[i])
    case.append(s[i+1])
    all_cases.append(case)
    i=i+2

all_symbols=[]
for i in range(len(all_cases)):
    symbols=[]
    for x in range(len(all_cases[i][0])):
        if all_cases[i][0][x]==all_cases[i][1][x]:
            symbols.append('.')
        else:
            symbols.append('*')
    all_symbols.append(symbols)


for i in range(len(all_cases)):
    for char in all_cases[i][0]:
        print(char, end='')
    print()
    for k in all_cases[i][1]:
        print(k, end='')
    print()
    for s in all_symbols[i]:
        print(s, end='')
    print()
    print()
#Accepted