## 
## country_codes.py
## @ianpasm(kno30826@gmail.com)
## 2018-03-26 10:57:59
## 
 
#!/usr/bin/env python3
# coding=utf-8

from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

#print(get_country_code('Andorra'))
#print(get_country_code('Afghanistan'))
#print(get_country_code('United Arab Emirates'))




