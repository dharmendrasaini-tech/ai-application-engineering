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









