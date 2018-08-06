#!/usr/bin/env python
# coding=utf-8
# 在Python中,字典是一系列的键值对
# 字典是由花括号括起来的,键值之间使用冒号分隔的,键值对之间是用逗号分开的
# vendor = {'factory':'Xiaomi','country':'China','CEO':'Leijun'}
# print(vendor['factory'],vendor['Country'])

# Today Xiaomi changed CEO to monster
# vendor = {'factory':'Xiaomi','country':'China','CEO':'monster'}
# new_CEO = vendor['CEO']
# print("The new CEO is:" + new_CEO + "!")

# Add key-value
# 字典是一种动态结构
# print(vendor)
# vendor['size'] = 10000
# vendor['distributeRange'] = 10
# print(vendor)

# Create null dict
vendor = {}
print(vendor)

vendor['size'] = 1000
vendor['CEO'] = 'Monster'
vendor['vendor'] = 'Xiaomi'
print(vendor)

# Modify the dict
vendor['size'] = 10000
vendor['CEO'] = 'Monley Lei'
print(vendor)

vendor['xpos'] = 10
vendor['ypos'] = 0
vendor['power'] = 'medium'
print("The origin xpos is:" + str(vendor['xpos']))
print("The origin ypos is:" + str(vendor['ypos']))

if vendor['power'] == 'weak':
    xincrement = -1
    yincrement = -1
elif vendor['power'] == 'medium':
    xincrement = 5
    yincrement = 5
else:
    xincrement = 10
    yincrement = 10

vendor['xpos'] = vendor['xpos'] + xincrement
vendor['ypos'] = vendor['ypos'] + yincrement
print("The new xpos is: " + str(vendor['xpos']))
print("The new ypos is: " + str(vendor['ypos']))

# Delete key-value
# 使用del语句时,必须指定字典名和要删除的键
print("\nDelete key-value foever!")
print(vendor)
del vendor['size']
print(vendor)
