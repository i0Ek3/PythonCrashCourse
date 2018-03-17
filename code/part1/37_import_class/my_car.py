## 
## my_car.py
## ianpasm(kno30826@gmail.com)
## 2017-11-21 17:02:24
## 
 
#!/usr/bin/env python3
# coding=utf-8

from car import Car

my_new_car = Car('audi','a7',2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
