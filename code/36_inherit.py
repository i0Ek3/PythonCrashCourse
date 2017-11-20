#!/usr/bin/env python
# coding=utf-8

#class Car(object): #python2.7
class Car(): #python3
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it!")

    def update_odometer(self):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("Cars have gas box!")

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self): # add describe_battery() method
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif slef.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self,make,model,year): 
        #super(ElectricCar,self).__init__(make,model,year) #python2.7
        super().__init__(make,model,year) #python3
        #self.battery_size = 70 # add attr
        self.battery = Battery()

    def describe_battery(self): # add describe_battery() method
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("The ElectricCar hasn't gas box!")



my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
