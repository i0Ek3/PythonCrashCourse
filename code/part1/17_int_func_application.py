#!/usr/bin/env python
# coding=utf-8
# 将数值输入用于比较和计算前,务必将其用int()函数转换成数值表示

height = input("How tall are you,in cm(s)? ")
height = int(height)

if height >= 165:
    print("\nYou're tall enough to ride!")
else:
    print("\nYour height too danger to ride,sorry!")
