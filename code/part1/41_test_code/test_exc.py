## 
## test_exc.py
## ianpasm(kno30826@gmail.com)
## 2017-11-26 10:25:19
## 
 
#!/usr/bin/env python3
# coding=utf-8

import unittest
from exc import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        addSlary = "How much would you like to added:"
        self.my_slary = Employee(addSlary)
        self.selects = [6000,10000]

    def test_give_default_raise(self):
        self.my_slary.give_raise(self.selects[0])
        self.assertIn(self.responses[0],self.my_slary.selects)

    def test_give_custom_raise(self):
        for select in self.selects:
            self.my_slary.give_raise(selects)
        for select in self.selects:
            self.assetIn(select,self.my_slary.selects)

unittest.main()
