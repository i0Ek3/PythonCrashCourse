## 
## reconstructor_remember_greet.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 08:45:56
## 
 
#!/usr/bin/env python3
# coding=utf-8

import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Whats your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We already remembered you," + username + "!")
else:
    print("Welcome back," + username + "!")
