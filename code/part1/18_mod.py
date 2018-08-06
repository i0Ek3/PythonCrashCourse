#!/usr/bin/env python
#coding=utf-8
#注意输出的时候需要用str()函数

a = input("Please input a num you want: \n")
b = input("Again: \n")
ret = int(a) % int(b)
print("I'll calculate the mod with your input nums!\n")
print("The mod is: " + str(ret) + " .")
