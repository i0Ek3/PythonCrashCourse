#!/usr/bin/env python
# coding=utf-8
# python 2.7将会显示age为具体数字,如22.
# 而python3将会显示字符串,如'22'
# python3下用int()函数进行这种关系的转换
# python2 use raw_input() to instead of python3's input()

#age = input("How old are you? ")
#print(age)

age = input("How old are you?")
age = int(age)
print(age)


