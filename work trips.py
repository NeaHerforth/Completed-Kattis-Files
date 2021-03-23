#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''2
7
saskatoon
toronto
winnipeg
toronto
vancouver
saskatoon
toronto
3
edmonton
edmonton
edmonton'''

s=s.splitlines()

n=int(s[0])

#Collect all citites in lists in a list
all_cases=[]
i=1
while i<len(s):
    cities=[]
    case_lenght=int(s[i])
    for x in range(i+1, i+ case_lenght+1):
        cities.append(s[x])
    all_cases.append(cities)
    i=i + case_lenght +1


#Find the number of distinct cities

for i in range(len(all_cases)):
    count={}
    for x in all_cases[i]:
        count.setdefault(x,0)
        count[x]=count[x]+1
    print(len(count.keys()))
#Accepted

