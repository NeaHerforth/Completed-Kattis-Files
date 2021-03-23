#! /usr/bin/env python3
import sys

#s=int(sys.stdin.read())

s='0 1 2 2 2 7'
s=s.split()
get=[]

#King=1
if int(s[0])==1:
    get.append(0)
elif int(s[0])>1:
    diff=int(s[0])-1
    kings=('-' + str(diff))
    get.append(kings)
elif int(s[0])<1:
    diff=str(1-int(s[0]))
    kings=diff
    get.append(kings)

#queens=1
if int(s[1])==1:
    get.append(0)
elif int(s[1])>1:
    diff=int(s[1])-1
    queens=('-' + str(diff))
    get.append(queens)
elif int(s[1])<1:
    diff=str(1-int(s[1]))
    queens=diff
    get.append(queens)

#Rooks=2
if int(s[2])==2:
    get.append(0)
elif int(s[2])>2:
    diff=int(s[2])-2
    rooks=('-' + str(diff))
    get.append(rooks)
elif int(s[2])<2:
    diff=str(2-int(s[2]))
    rooks=diff
    get.append(rooks)

#Bishop=2
if int(s[3])==2:
    get.append(0)
elif int(s[3])>2:
    diff=int(s[3])-2
    bishop=('-' + str(diff))
    get.append(bishop)
elif int(s[3])<2:
    diff=str(2-int(s[3]))
    bishop=diff
    get.append(bishop)

#knight=2
if int(s[4])==2:
    get.append(0)
elif int(s[4])>2:
    diff=int(s[3])-2
    knight=('-' + str(diff))
    get.append(knight)
elif int(s[4])<2:
    diff=str(2-int(s[4]))
    knight=diff
    get.append(knight)

#pawn=8
if int(s[5])==8:
    get.append(0)
elif int(s[5])>8:
    diff=int(s[5])-8
    pawn=('-' + str(diff))
    get.append(pawn)
elif int(s[5])<8:
    diff=str(8-int(s[5]))
    pawn=diff
    get.append(pawn)



for i in get:
    print(i, end= ' ')


#not accepted, but chess2.py is accpeted

