#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

#I created a text file with the input called 'tarifa.txt'
#the follwoing two lines are deleted and replaced with the above s=.... line
s=open('/Users/neaherforth/ITU/Python rematch/VScodium files/Repetition code/Automate the boring + EXERCISES/Text files/tarifa.txt')
s=s.read().splitlines()

#Number of megabytes to use per month
X=int(s[0])

#First N months
N=int(s[1])

#Amount spend in the following months
spend=[]
for i in range(2,len(s)):
    spend.append(s[i])

left=0
for i in spend:
    left= left + X 
    left = left-int(i)

#For the N+1 month X amount of megabytes is added again
left=left+X
print(left)

#Accepted

