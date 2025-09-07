# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 23:36:42 2025

@author: hp
"""

print("pattern 1")
n=int(input("enter number of rows:"))
for i in range(0,n+1):
        print(" " * (n-i),end=" ")
        print("*" *(2*i-1))
        
print("pattern 2")
n=int(input("enter number of rows:"))
for i in range(n,0,-1):
    print(" " * (n-i),end=" ")
    print("*" * (2*i-1))
    
print("pattern 3")
n=int(input("enter number of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()

print("pattern 4")
n=int(input("enter number of rows:"))    
for i in range(0,n+1):
    for j in range (1,i+1):
       print(j,end="")
    print()
    

print("pattern 5")
n=int(input("enter number of rows:"))    
for i in range(0,n+1):
    for j in range (1,i+1):
       print(i,end="")
    print()