## 
## greet.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 08:40:35
## 
 
#!/usr/bin/env python3
# coding=utf-8

import json

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back," + username + "!")
