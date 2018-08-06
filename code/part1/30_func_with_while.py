#!/usr/bin/env python
# coding=utf-8

def get_name(firstname,lastname):
    name = firstname + ' ' + lastname
    return name.title()

while True:
    print("\nPlease tell me your name(Enter 'q' to end):")
    firstname = input("FirstName: ")
    if firstname == 'q':
        break

    lastname = input("LastName: ")
    if lastname == 'q':
        break
    iname = get_name(firstname,lastname)
    print("\nHello " + iname)

