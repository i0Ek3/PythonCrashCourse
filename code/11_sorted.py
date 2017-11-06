#!/usr/bin/env python
# coding=utf-8
# 

dict = {'color':190,'size':250,'point':5}
print(dict)
print("The sorted list value like this: ")
for x in sorted(dict.values()):
    print(x)

print("The sorted list key like this: ")
for y in sorted(dict.keys()):
    print(y)
