#! /usr/bin/env python3
import sys
#s=str(sys.stdin.read())

s='2 3 4 5 1'
numbers=s.split()

def swap(numbers):
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            #delete i and insert at index i+1
            num=numbers[i]
            del numbers[i]
            numbers.insert(i+1, num)
            print(' '.join(numbers))

#n=' '.join(numbers)
while True:
    if ' '.join(numbers)=='1 2 3 4 5':
        break
    else:
        swap(numbers)

#Accepted
