#!/usr/bin/env python
# coding=utf-8

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage): #2
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            self.odometer_reading = mileage
    
    def increment_odometer(self,miles): #3
        self.odometer_reading += miles

my_new_car = Car('audi','a6',2017)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# way1 to modified value of property
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# way2
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# way3
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(222000)
print(my_used_car.read_odometer())

my_used_car.increment_odometer(100)
print(my_used_car.read_odometer())

