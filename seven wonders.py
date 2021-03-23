#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='TTTCCCGGG'
cards={}
for i in s:
    cards.setdefault(i, 0)
    cards[i]=cards[i]+1

#Calculate base points
points=0
for val in cards.values():
    points=points + int(val)**2

#Calculate extra points - if all values are in the dict, then the lowest number is 
#.. the number of sets (that contain all three cards)
if 'T' in cards.keys() and 'C' in cards.keys() and 'G' in cards.keys() :
    min_number=min(cards.values())
    bonus=min_number*7
else:
    bonus=0

print(points + bonus)