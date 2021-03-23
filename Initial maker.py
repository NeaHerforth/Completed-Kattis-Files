#! /usr/bin/env python3
import sys

s=str(sys.stdin.read()) ###remember to write input like this in kattis
#s='Pasko-Patak'

initial=''
for i in s.split('-'):
    initial = initial + i[0]
print(initial)

#Accepted