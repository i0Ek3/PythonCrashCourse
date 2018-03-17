#!/usr/bin/env python
# coding=utf-8

#1 传递任意多的实参
# *temple用来创建一个temple空元祖
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepper')
make_pizza('beef','sausage','green')


#2
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("--> " + topping)

make_pizza('pepper')
make_pizza('beef','sausage','green')


#3 #2 with position arguments
def make_pizza(size,*toppings):
    print("\nMaking a pizza with " + str(size) + "-inch with the following toppings:")
    for topping in toppings:
        print("--> " + topping)

make_pizza(16,'pepper')
make_pizza(88,'beef','sausage','green')


#4 use key argument arbitrarily
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',
        location='princeton',field='physics'
        )
print(user_profile)
