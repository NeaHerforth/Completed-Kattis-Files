#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s='''3
0 100 70
100 130 30
-100 -7 40'''

s=s.splitlines()

for i in range(1, len(s)):
    line=s[i].split()
    no_ad_rev=int(line[0])
    ad_rev=int(line[1])
    cost=int(line[2])

    no_ad_sum=no_ad_rev
    ad_sum=ad_rev-cost
    print(no_ad_sum, ad_sum)
    if no_ad_sum>ad_sum:
        print('do not advertise')
    elif no_ad_sum==ad_sum:
        print('does not matter')
    elif ad_sum>no_ad_sum:
        print('advertise')

