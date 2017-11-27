## 
## number_writer.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 08:27:34
## 
 
#!/usr/bin/env python3
# coding=utf-8

import json

def writer():
    numbers = [1,3,5,7,9]

    filename = 'numbers.json'
    with open(filename,'w') as f_obj:
        json.dump(numbers,f_obj)

def reader():
    filename = 'numbers.json'
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
    print(numbers)

writer()
reader()

