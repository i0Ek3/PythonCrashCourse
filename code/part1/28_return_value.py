#!/usr/bin/env python
# coding=utf-8

# return simple value 
def get_name(firstname,lastname):
    name = firstname + ' ' + lastname
    return name.title()

actor = get_name('miky','jhson')
print(actor)

# argument selectable
def get_name(firstname,middlename,lastname):
    name = firstname + ' ' + middlename + ' ' + lastname
    return name.title()

actor = get_name('miky','rk','jhson')
print(actor)

#
def get_name(firstname,lastname,middlename=''):
    if middlename:
        name = firstname + ' ' + middlename + ' ' + lastname
    else:
        name = firstname + ' ' + lastname
    return name.title()

actor = get_name('jimi','kod')
print(actor)
actor = get_name('jimi','joe','d')
print(actor)
        
