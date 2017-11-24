## 
## test_name_function.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 17:37:38
## 
 
#!/usr/bin/env python3
# coding=utf-8

import unittest
from name_function import get_formatted_name2

class NamesTestCase(unittest.TestCase):
    """ test name_function.py"""

    def test_first_last_name(self):
        """deal with name like under this""" 

        formatted_name = get_formatted_name2('janis','joplin','heool')
        self.assertEqual(formatted_name,'Janis Heool Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name2('marry','kelin','berrh')
        self.assertEqual(formatted_name,'Marry Berrh Kelin')

unittest.main()
