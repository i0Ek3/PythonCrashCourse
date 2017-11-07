#!/usr/bin/env python
# coding=utf-8

# 列表和字典不应该有太多的嵌套层级,不然会有更简单的解决办法!

users = {
    'kjames':{
        'first':'corden',
        'last':'james',
        'address':'neweston',
        },
    'ojhon':{
        'first':'jeo',
        'last':'jhon',
        'address':'bominghan',
        },
    } 

for username,user_info in users.items():
    print("\nUsername: " + username)
    fullname = user_info['first'] + " " + user_info['last']
    address = user_info['address']

    print("\tFull name: " + fullname.title())
    print("\tAddress: " + address.title())
