## 
## reconstructor_remember_greet.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 08:52:52
## 
 
#!/usr/bin/env python3
# coding=utf-8

import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    filename = 'username.json'
    username = input("Whats your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = get_new_username()
        print("We already remembered you," + username + "!")

greet_user()
