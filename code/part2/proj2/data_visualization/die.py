## 
## die.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-21 10:17:18
## 
 
#!/usr/bin/env python3
# coding=utf-8

from random import randint

class Die():
    """express a class of dicing"""

    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """return a value between 1 and num_sides"""

        return randint(1,self.num_sides)
