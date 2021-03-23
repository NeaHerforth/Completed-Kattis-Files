#! /usr/bin/env python3
import sys

#n=int(sys.stdin.read())
# how to find the number of points
#0.  felter->  1*1=1    / punkter->  (1+1)*(1+1) = 4
#1.  felter-> 2*2=4     / punkter-> (2+1)*(2+1)= 9
#2.  felter-> 4*4=16    / punkter-> (4+1)*(4+1)=25
#3.  felter-> 8*8=64    / punkter-> (8+1)*(8+1)=81
#4. felter-> 16*16=256  / punkter-> (16+1)*(16+1)= 289
#5. felter-> 32*32= 1024 / punkter-> (32+1)*(32+1)=1089!!

#the relation between n (iterations) and number of squares
#0. 2^0 = 1
#1. 2^1 = 2
#2. 2^2 = 4 
#3. 2^3 = 8
#4. 2^4 = 16
#5. 2^5 = 32

n=2

fields=2**n
points = (fields + 1)* (fields + 1)
print(points)

