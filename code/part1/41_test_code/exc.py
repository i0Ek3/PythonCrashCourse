## 
## exc11-3.py
## ianpasm(kno30826@gmail.com)
## 2017-11-26 10:19:06
## 
 
#!/usr/bin/env python3
# coding=utf-8

class Employee():

    def __init__(self,firstname,lastname,slary):
        self.firstname = firstname 
        self.lastname = lastname
        self.slary = slary
        self.select = []

    def give_raise(self,slary=5000):
        addSlary = input("How much slary would you like to added?Maybe you relize it:")
        self.slary += str(addSlary)
