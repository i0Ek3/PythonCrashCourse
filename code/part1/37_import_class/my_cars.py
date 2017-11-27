## 
## my_cars.py
## ianpasm(kno30826@gmail.com)
## 2017-11-21 19:00:04
## 
 
#!/usr/bin/env python3
# coding=utf-8


# import part classes
from car import Car,ElectricCar

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

# import all classes
import car

my_beetle = car.Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())


