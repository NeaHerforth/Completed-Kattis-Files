#! /usr/bin/env python3
import sys

#n=str(sys.stdin.read())

n='Welcome_NWERC_participants!'

white=0.0
lower=0.0
upper=0.0
symbols=0.0
total=0.0

for i in n:
    if i== '_':
        white +=1
    elif i.islower():
        lower+=1
    elif i.isupper():
        upper +=1
    else:
        symbols +=1
    total +=1

ratio_white = white/total
ratio_lower = lower/total
ratio_upper = upper/ total
ratio_symbol = symbols/ total

#ratio_white= format(ratio_white, '.16f')
#ratio_lower= format(ratio_lower, '.16f')
#ratio_upper= format(ratio_upper, '.16f')
#ratio_symbol= format(ratio_symbol, '.16f')

print(ratio_white)
print(float(ratio_lower))
print(str(ratio_upper))
print(str(ratio_symbol))


#0.0740740740740741
#0.666666666666667
#0.222222222222222
#0.0370370370370370







