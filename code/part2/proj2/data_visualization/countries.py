## 
## countries.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-26 10:55:50
## 
 
#!/usr/bin/env python3
# coding=utf-8

from pygal.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])



