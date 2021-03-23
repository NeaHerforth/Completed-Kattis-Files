#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''4
A
A
A
A'''
s=s.splitlines()

correct_answers=[]
for i in range(1, len(s)):
    correct_answers.append(s[i])

import copy
answers=copy.copy(correct_answers)
del answers[0]
answers.append(0)

points=0
for i in range(len(answers)):
    if correct_answers[i]==answers[i]:
        points+=1
print(points)
