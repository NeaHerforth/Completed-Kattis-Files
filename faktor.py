#! /usr/bin/env python3
import sys
s=str(sys.stdin.read())

#s='10 10'
s=s.split()

#Number of articles you post
articles=float(s[0])

#Impact faktor
faktor=float(s[1])-0.99


#Equation -> citation/articles=faktor
#citations = articles * faktor

import math

citations = articles*faktor
citations=math.ceil(citations)
print(citations)

#Accepted