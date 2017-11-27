#!/usr/bin/env python
# coding=utf-8

# Instance
#   def func(parameter list):
#        print("")
#
#   func(argument list)

# Position Argument
"""即要求实参的顺序和形参的顺序相同"""

def describe1(type,name):
    print("I have a " + type + ".")
    print("My " + type + "'s name is " + name + ".")

describe1('dog','bobby')
describe1('cat','shit')

# Key Argument
"""它是传递给函数的名称-值对"""
"""而不在关注实参的顺序"""

def describe2(type,name):
    print("I have a " + type + ".")
    print("My " + type + "'s name is " + name + ".")

describe2(type='dog',name='bobby')
describe2(name='shit',type='cat')

# Default Vaule
"""若在调用函数中给形参提供了实参"""
"""python将使用指定的实参值,否则将使用形参的默认值"""
"""因此,给形参指定默认值后,可在函数调用中省略相应的实参"""

# 注意将name应放在第一位置
# 即使用默认值时,在形参列表中必须先列出没有默认值的形参
def describe3(name,type='dog'):
    print("I have a " + type + ".")
    print("My " + type + "'s name is " + name + ".")

describe3(name='doge')

# Excise1
# make_shirt()
# position argument
def make_shirt(size,print_text):
    print("The T-Shirt's size is: " + size + ",and text:" + print_text + " will be print!")
make_shirt('XXXL','Hello,Python!')

# key argument
def make_shirt(size='M',print_text='Boom Shit!'):
    print("The T-Shirt's size is: " + size + ",and text:" + print_text + " will be print!")
make_shirt()

# Excise2
# describe_city()
def describe_city(city,country='Cuba'):
    print(city + " is in " + country)
describe_city('Havana')



