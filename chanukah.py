#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
1 8
2 1
3 10'''

s=s.splitlines()

#P is the number of datasets
P=int(s[0])

#Make a list of the days 
days=[]
for i in range(1,P+1):
    day=s[i].split()
    days.append(day[1])

#Find out how many candles are needed for each case
for i in range(len(days)):
    candles=0
    for x in range(int(days[i])+1):
        candles= candles + int(x)
    candles = candles + int(days[i])
    print( str(i+1)+ ' '+ str(candles))

#Accepted!