## 
## name_function.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 17:30:13
## 
 
#!/usr/bin/env python3
# coding=utf-8

def get_formatted_name(first,middle,last):
    """generate formatted name"""

    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    
    return full_name.title()
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

def get_formatted_name1(first,middle,last):
    """generate formatted name"""

    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    
    return full_name.title()
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

def get_formatted_name2(first,last,middle=''):
    """generate formatted name"""

    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    
    return full_name.title()
