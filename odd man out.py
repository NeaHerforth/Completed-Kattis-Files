#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
3
1 2147483647 2147483647
5
3 4 7 4 3
5
2 10 2 10 5'''

s=s.splitlines()

#Numebr of cases
n=int(s[0])

#sort out the C numbers in lists in a list
guests=[]
i=2
while i<len(s):
    c=[]
    guest=s[i].split()
    for x in guest:
        c.append(x)
    guests.append(c)
    i=i+2

#See if a number C appears twice in each list, otherwise print it
for i in range(len(guests)):
    count={}
    for l in guests[i]:
        count.setdefault(l,0)
        count[l]=count[l]+1
    #Make two seperate lists for keys and values
    key_list = list(count.keys())
    val_list = list(count.values())
    #find the minimum value and its index - this is the odd man out
    min_value=min(val_list)
    position = val_list.index(min_value)
    #Print out each 
    print('Case #' + str(i+1)+': '+ key_list[position])
#Accepted