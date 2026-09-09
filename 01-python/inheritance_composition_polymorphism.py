# 🚗 Sep 6 Mini OOP Model — Vehicle Service Center
# Problem

# You are building a small domain model for a vehicle service center.

# The service center works with different types of vehicles. All vehicles share some common state and behavior, but different vehicle types behave differently when they are serviced.

# A vehicle also has an engine, so the engine should be modeled as a separate object rather than putting all engine behavior directly inside the vehicle.

# Your model must demonstrate:

# inheritance
# method overriding
# super()
# composition
# delegation
# polymorphism
# 1. Engine

# Create a class:

# Engine
# Instance attributes
# engine_type
# running

# When created:

# running = False
# Methods
# start()

# Changes:

# running = True
# stop()

# Changes:

# running = False
# is_running()

# Returns the current engine state.

# 2. Vehicle

# Create the parent class:

# Vehicle
# Instance attributes

# Every vehicle has:

# brand
# model
# engine

# engine must be an Engine object.

# Example conceptually:

# engine = Engine("Petrol")
# car = ...
# Methods
# start_vehicle()

# The vehicle should ask its engine to start.

# Do not directly modify:

# engine.running

# Use delegation.

# stop_vehicle()

# Ask the engine to stop.

# get_service_message()

# Returns:

# "Performing standard vehicle service."
# 3. Car

# Create:

# Car(Vehicle)

# A car IS-A Vehicle.

# Additional instance attribute
# number_of_doors

# Use super() when initializing the inherited vehicle state.

# Override

# Override:

# get_service_message()

# It should return:

# "Servicing car."
# 4. ElectricCar

# Create:

# ElectricCar(Car)

# An electric car:

# IS-A Car
# IS-A Vehicle
# Additional attribute
# battery_percentage

# Rules:

# 0 <= battery_percentage <= 100

# Otherwise raise:

# ValueError

# Use super() for the inherited initialization.

# Override

# Override:

# get_service_message()

# Return:

# "Checking electric car battery and motor."
# 5. Motorcycle

# Create:

# Motorcycle(Vehicle)
# Additional attribute
# has_sidecar

# It should be a boolean.

# Use super() for the inherited vehicle state.

# Override
# get_service_message()

# Return:

# "Servicing motorcycle."
# 6. Polymorphic Function

# Create a standalone function:

# service_vehicle(vehicle)

# The function should not check the concrete type.

# ❌ Do not write:

# if isinstance(vehicle, Car):
#     ...
# elif isinstance(vehicle, Motorcycle):
#     ...

# Instead, rely on the behavioral interface:

# vehicle.get_service_message()

# The function should return whatever service message the object provides.

# This means the same function should work with:

# Vehicle
# Car
# ElectricCar
# Motorcycle

# without knowing their concrete types.

# 7. Required Test Scenario

# Create:

# Engine("Petrol")
# Engine("Electric")
# Engine("Petrol")

# Then create:

# Car
# ElectricCar
# Motorcycle

# Use any brands/models you like.

# For example, your objects could represent:

# BMW car
# Tesla electric car
# Royal Enfield motorcycle

# Then prove that:

# service_vehicle(car)
# service_vehicle(electric_car)
# service_vehicle(motorcycle)

# produces different behavior through the same interface.

# Also demonstrate:

# car.start_vehicle()

# and verify that its composed Engine object is now running.

# Engineering constraints ⚙️

# For this exercise:

# Use:

# classes and objects
# instance attributes
# inheritance
# overriding
# super()
# composition
# delegation
# polymorphism
# basic validation
# ValueError

# Do not use yet:

# @dataclass
# abstract base classes
# protocols
# decorators
# custom dunder methods
# multiple inheritance
# advanced typing

# Those would hide the fundamentals we're trying to prove today.

# Definition of Done

# Your project is complete when you can explain these relationships:

# Vehicle
# ├── Car
# │   └── ElectricCar
# └── Motorcycle

# and:

# Vehicle HAS-A Engine

# and you can explain why this works:

# service_vehicle(car)
# service_vehicle(electric_car)
# service_vehicle(motorcycle)

# without service_vehicle() knowing the concrete type.

# That last part is the core polymorphism proof.

        

class Engine:
    def __init__(self,engine_type):

        self.engine_type = engine_type
        self.running = False


    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def is_running(self):
        return self.running




class Vehicle:

    def __init__(self,brand,model,engine):
        self.brand = brand
        self.model = model
        self.engine = engine


    def start_vehicle(self):
        return self.engine.start()

    def stop_vehicle(self):
        return self.engine.stop()

    def get_service_message(self):
        return "Performing standard vehicle service."



class Car(Vehicle):
    def __init__(self,brand, model, engine,number_of_doors):

        super().__init__(brand,model,engine)

        self.number_of_doors = number_of_doors


    def get_service_message(self):
        return "Servicing car"



class ElectricCar(Car):

    def __init__(self,brand,model,engine,number_of_doors,battery_percentage):

        super().__init__(brand,model,engine,number_of_doors)

        if battery_percentage < 0 or battery_percentage > 100:
            raise ValueError("Invalid battery percentage")


        self.battery_percentage = battery_percentage


    def get_service_message(self):
        return "Checking electric car battery and motor."



class Motorcycle(Vehicle):

    def __init__(self,brand,model,engine,has_sidecar):

        super().__init__(brand,model,engine)


        self.has_sidecar = has_sidecar


    def get_service_message(self):
        return "Servicing motorcycle"

    


def service_vehicle(vehicle):
    return vehicle.get_service_message()




petrol_engine = Engine("Petrol")
electric_engine = Engine("Electric")
motorcyle_engine = Engine("Petrol")


bmw_car = Car("BMW",2018,petrol_engine,4)
tesla_electric_car = ElectricCar("Tesla",2020,electric_engine,4,60)
royal_enfield_motorcycle = Motorcycle("Royal Enfield",2021,motorcyle_engine,True)



print(service_vehicle(bmw_car))
print(service_vehicle(tesla_electric_car))
print(service_vehicle(royal_enfield_motorcycle))

print(bmw_car.engine.is_running())

bmw_car.start_vehicle()

print(bmw_car.engine.is_running())

































#VERSION 2


class Engine:
    def __init__(self,engine_type):

        self.engine_type = engine_type
        self.running = False



    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def is_running(self):
        return self.running




class Vehicle:
    def __init__(self,brand,model,engine):
        self.brand = brand
        self.model = model
        self.engine = engine


    def start_vehicle(self):
        self.engine.start()

    def stop_vehicle(self):
        self.engine.stop()

    def get_service_message(self):
        return "Vehicle serviced."



class Car(Vehicle):
    def __init__(self,brand,model,engine,doors):

        super().__init__(brand,model,engine)

        self.doors = doors


    def get_service_message(self):
        return "Car serviced."


class MotorCycle(Vehicle):
    def __init__(self,brand,model,engine,has_sidecar):
        super().__init__(brand,model,engine)

        self.has_sidecar = has_sidecar


    def get_service_message(self):
        return "MotorCycle serviced."
    


def service_vehicle(vehicle):
    return vehicle.get_service_message()

   
#1
petrol_engine = Engine("petrol")

print(petrol_engine.isrunning())


#2
car = Car("skoda","kylaq",petrol_engine,4)

print(car.start_vehicle())

print(petrol_engine.is_running())

#3
print(car.stop_vehicle())
print(petrol_engine.is_running())

#4
diesel_engine = Engine("diesel")

print(diesel_engine.engine_type)
print(petrol_engine.engine_type)

#5

motorcycle = MotorCycle("Honda","Shine",diesel_engine,False)

print(car.brand)
print(car.model)
print(motorcycle.brand)
print(motorcycle.model)

#6
print(car.doors)
print(motorcycle.has_sidecar)

#7

print(service_vehicle(car))
print(service_vehicle(motorcycle))


#8
vehicle = Vehicle("Honda","City",diesel_engine)
print(service_vehicle(vehicle))

#9

# Because python return None for a function which does not return anything.

# 8.6 answers

#1 Because Vehicle has an engine . So the relations is more suited for composition.

#2 Becuase they are vehicles.

#3 Inside the engine, because running is a behaviour of engine not vehicle.

#4 print(car.stop_vehicle())
# print(petrol_engine.isrunning())

#5 get_service_message(self)

#6 the object passed must provide a callable get_service_message() method.

#7 Yes because python does not care about the type unless it provides the required behaviour through its method

#8 Yes , composition will make it easier to replace the dependency






