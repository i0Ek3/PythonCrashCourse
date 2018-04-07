## 
## names.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 17:31:36
## 
 
#!/usr/bin/env python3
# coding=utf-8

from name_function import get_formatted_name

print("Enter 'q' to quit!")
while True:
    first = input("Plz input your first name:")
    if first == 'q':
        break

    last = input("Plz input your second name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print("\tNeatly formatted name: " + formatted_name + ".")
