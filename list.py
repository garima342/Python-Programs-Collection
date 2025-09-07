# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 23:22:54 2025

@author: hp
"""

a=[10,20,30,40,50]
a.append(60)
print("append:",a)

b=[70,80,90,100]
a.extend(b)
print("extend",a)

a.insert(0,5)
print("insert",a)

a[1]=11
print("update",a)

a.remove(5)
print("remove",a)

a.pop()
print("pop",a)

a.pop(3)
print("index pop",a)

a.reverse()
print("reverse",a)

c=[23,65,33,21,3,0]
c.sort()
print("sort",c)

a.sort(reverse=True)
print("descending",a)

d=a.copy()
print("copy",d)

a.clear()
print("list is clear")