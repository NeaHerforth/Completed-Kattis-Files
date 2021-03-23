#! /usr/bin/env python3
import sys
#s=str(sys.stdin.read())

s='12 20'
s=s.split()

#N is the firt dice (first value in string), M is the second dice.
N=int(s[0])
M=int(s[1])

#Make a list that contains all possible numbers the dice can land on, for each die
#1. Dice N 
N_sides=[]
for i in range(N):
    N_sides.append(i+1)

#2. Dice M
M_sides=[]
for i in range(M):
    M_sides.append(i+1)

#create a lists that contains all possible sums of the two die.
sums=[]
for i in N_sides:
    for x in M_sides:
        sums.append(i+x)
sums.sort()


#Counts each value in the list. The sum is the key, the count is the value 
count={}
for i in sums:
    count.setdefault(i, 0)
    count[i] = count[i] + 1 


# Find item with Max Value in Dictionary
MaxValue = max(count.items(), key=lambda x: x[1])
listOfKeys = list()

# Iterate over all the items in dictionary to find keys with max value
for key, value in count.items():
    if value == MaxValue[1]:
        listOfKeys.append(key)

#Print each value in the list of keys on a new line        
for i in listOfKeys:
    print(i)




