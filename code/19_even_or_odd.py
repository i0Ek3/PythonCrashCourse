#!/usr/bin/env python
# coding=utf-8

number = input("Please input a number,I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number you input: " + str(number) + " is even.")
else:
    print("\nThe number you input: " + str(number) + " is odd.")
