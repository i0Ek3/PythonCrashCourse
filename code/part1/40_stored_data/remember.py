## 
## remember.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 08:35:01
## 
 
#!/usr/bin/env python3
# coding=utf-8

import json

username = input("Whats your name?")

filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We already remember you," + username + ".")
