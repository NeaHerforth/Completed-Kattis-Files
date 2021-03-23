#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['0 0 1']
cards=s[0].split()

#Define the cards
gold=int(cards[0])
silver=int(cards[1])
copper=int(cards[2])

def get_points(gold, silver, copper):
    points=gold*3 +silver*2 + copper*1
    return points

points=get_points(gold, silver, copper)

#Find out what the best card that you can get is
if points<2:
    print('Copper')
elif points<3:
    print('Estate or Copper')
elif points<5:
    print('Estate or Silver')
elif points<6:
    print('Duchy or Silver')
elif points<8:
    print('Duchy or Gold')
else:
    print('Province or Gold')
#Accepted
