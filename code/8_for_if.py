#!/usr/bin/env python
# coding=utf-8

# 多层嵌套循环

nexuss = ['nexus 1','nexus 4','nexus 5','nexus 6','nexus 7']
print("Google producted so many nexus products,like this:")
print(nexuss)
for nexus in nexuss:
    if nexus == 'nexus 1':
        print(nexus + ",this product is too old to use!")
    elif nexus == 'nexus 6':
        print(nexus + ",this is my phone ,its so beautiful.")
    elif nexus == 'nexus 4':
        print("I still have nexus 4 with Sailfish OS,good device!")
    elif nexus == 'nexus 7':
        print("I still have nexus 7 with Ubuntu touch,good device!")
    elif nexus == 'nexus 5':
        print("I have not nexus 5!")
print("Which one do you liked?")
