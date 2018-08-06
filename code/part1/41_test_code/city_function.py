## 
## exc1.py
## ianpasm(kno30826@gmail.com)
## 2017-11-24 19:13:27
## 
 
#!/usr/bin/env python3
# coding=utf-8

#11-1

def city(cityname='Santiago',countryname='Chile'):
        #print("Enter 'q' to quit!")
        
        #while True:
        #    cityname = input("Please input a city which you liked:")
        #    if cityname == 'q':
        #        break
    
        #    countryname = input("Please input the country which you input city belonged to:")
        #    if countryname == 'q':
        #        break

        name = cityname.title() + "," + countryname.title() + "."
        return name
