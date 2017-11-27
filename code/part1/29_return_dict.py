#!/usr/bin/env python
# coding=utf-8

#
def return_dict(firstname,middlename,lastname):
    person = {'first':firstname,
            'middle':middlename,
            'last':lastname}
    return person

actor = return_dict('josh','k','moby')
print(actor)

#
def return_dict(firstname,lastname,age=''):
    person = {'first':firstname,
            'last':lastname}
    if age:
        person['age'] = age
    return person

actor = return_dict('jooh','migo',age=23)
print(actor)
    
