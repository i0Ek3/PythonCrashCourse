#!/usr/bin/env python
# coding=utf-8

# File "34_dog_class.py", line 15
#    mydog = Dog('bill',3)
#        ^
# SyntaxError: invalid syntax

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(str(self.name.title() + " rolled overed.")

mydog = Dog('bill',3)
youdog = Dog('lisa',4)

print("My dog's name is " + mydog.name.title() + ".")
print("My dog is " + str(mydog.age) + " years old.")
print("You dog's name is " + youdog.name.title() + ".")
print("You dog is " + str(youdog.age) + " years old.")

mydog.sit()
youdog.sit()
mydog.roll_over()
youdog.roll_over()
