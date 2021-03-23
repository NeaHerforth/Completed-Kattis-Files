#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''300
500'''

s=s.splitlines()

#Put each digit into a list so numbers can be compared
dig1=[]
dig2=[]

for i in s[0]:
    dig1.append(i)

for i in s[1]:
    dig2.append(i)

#Find longest list, and make the other one as long
maxlenght=0
if len(dig1)>len(dig2):
    maxlenght=len(dig1)
else:
    maxlenght=len(dig2)

#Find difference between lists
newdig1=[]
newdig2=[]
diff=abs(len(dig1)-len(dig2))

#Make digit one comparable
if len(dig1)==maxlenght:
    for i in dig1:
        newdig1.append(i)
else:
    newdig1=[0]*diff
    for i in dig1:
        newdig1.append(i)

#Make digit two comparable
if len(dig2)==maxlenght:
    for i in dig2:
        newdig2.append(i)
else:
    newdig2=[0]*diff
    for i in dig2:
        newdig2.append(i)

#Compare the two numbers and create new numbers
fin1=[]
fin2=[]
for i in range(maxlenght):
    if int(newdig1[i])>int(newdig2[i]):
        fin1.append(newdig1[i])
    elif int(newdig1[i])==int(newdig2[i]):
        fin1.append(newdig1[i])
        fin2.append(newdig2[i])
    else:
        fin2.append(newdig2[i])

#Convert the lists into strings and print the number or 'YODA'
final1=''.join(fin1)
final2=''.join(fin2)

if final1=='':
    print('YODA')
else:
    print(int(final1))

if final2=='':
    print('YODA')
else:
    print(int(final2))

#Accepted - 2 points!!