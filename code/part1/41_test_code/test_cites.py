## 
## test_cites.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 19:19:36
## 
 
#!/usr/bin/env python3
# coding=utf-8

import unittest
from city_function import city

class CityFunctionTest(unittest.TestCase):
    """Test city"""

    def test_city_country(self):
        namecity = city('santiago','chile')
        self.assertEqual(namecity,'Santiago,Chile.')

unittest.main()
