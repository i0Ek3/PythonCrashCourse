#!/usr/bin/env python
# coding=utf-8
# 

dict = {'color':190,'size':250,'point':5,'size':250}
print(dict)
print("The sorted list value like this: ")
for x in sorted(dict.values()): #排序
    print(x)

print("The sorted list key like this: ")
for y in sorted(dict.keys()):
    print(y)

print("The set list key like this: ")
for y1 in set(dict.keys()): #去重 
    print(y1)
print("The set  list key like this: ")
for y2 in set(dict.values()):
    print(y2)
