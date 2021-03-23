#! /usr/bin/env python3
import sys
#s=sys.stdin.read().splitlines()

s=['47']
dig=int(s[0])

#Convert into binary - has prefix '0b'
binary=bin(dig)

#Make it a list and reverse the list
binlist=list(binary)
binlist.reverse()

#Remove the prefix
del binlist[-1]
del binlist[-1]

#Make the reversed list a string and ad the binary prefix 0b again
reversebin=''.join(binlist)
reversebin='0b'+reversebin


print(int(reversebin, base=0))
#Accepted