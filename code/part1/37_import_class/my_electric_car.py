## 
## my_electric_car.py
## ianpasm(kno30826@gmail.com)
## 2017-11-21 18:18:55
## 
 
#!/usr/bin/env python3
# coding=utf-8

from car import ElectricCar

my_tesla = ElectricCar('tesla','model s',2017)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
