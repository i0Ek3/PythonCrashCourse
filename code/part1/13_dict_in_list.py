#!/usr/bin/env python
# coding=utf-8

#存储所点pizza的信息

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }

#概述所点的pizza
print("You ordered a " + pizza['crust'] + "-crust pizza" + " with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
print("\n")

favorite_languages = {
        'jen':['python','ruby'],
        'sarah':['c','c++'],
        'pilip':['go','haskell'],
        'edward':['perl','vala'],
        }
print(favorite_languages)
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

