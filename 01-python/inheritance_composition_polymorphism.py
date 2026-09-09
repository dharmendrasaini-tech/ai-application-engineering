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



# 8. End-of-Day Deliverable: Mini OOP Model
# This is the required Day 2 roadmap deliverable. Build one small Vehicle Service model that demonstrates all Day 2 concepts together. Do not use dataclasses, abstract base classes, advanced dunder methods, decorators, or external libraries.
# Submission standard
# Before coding, draw the relationships. After coding, run the verification scenarios. Be able to point to the exact line where inheritance, composition, delegation, overriding, and polymorphism occur.

# 8.1 Required classes
# Class	Responsibility	Required state / behavior
# Engine	Own engine running state	engine_type, running; start(), stop(), is_running()
# Vehicle	Base vehicle behavior and Engine dependency	brand, model, engine; start_vehicle(), stop_vehicle(), get_service_message()
# Car	Specialized Vehicle	doors; override get_service_message()
# Motorcycle	Specialized Vehicle	has_sidecar; override get_service_message()

# 8.2 Required relationships
# •	Car inherits from Vehicle.
# •	Motorcycle inherits from Vehicle.
# •	Vehicle receives an Engine object through its constructor and stores it as an instance dependency.
# •	Vehicle delegates start/stop work to the Engine object.
# •	Car and Motorcycle override get_service_message().
# •	A standalone service_vehicle(vehicle) function calls vehicle.get_service_message() without branching on concrete type.
# 8.3 Required behavior and rules
# •	Engine.running starts as False.
# •	Engine.start() changes running to True; Engine.stop() changes it to False.
# •	Vehicle.start_vehicle() must use the contained Engine rather than duplicate engine state on Vehicle.
# •	Vehicle.stop_vehicle() must delegate to Engine.stop().
# •	Vehicle base implementation returns a general service message.
# •	Car returns a car-specific service message.
# •	Motorcycle returns a motorcycle-specific service message.
# •	Subclass constructors must initialize Vehicle state correctly and then add their own state.
# •	Do not use isinstance() branches inside service_vehicle() to choose the message.
# 8.4 Suggested object relationship diagram
# Vehicle  -- has-a -->  Engine
#    ^
#    | inheritance (is-a)
#    +-----------+
#    |           |
#   Car     Motorcycle

# service_vehicle(x)
#         |
#         +--> calls x.get_service_message() polymorphically

# 8.5 Minimum verification scenarios
# •	Create one Engine and confirm it starts with running == False.
# •	Create a Car with that Engine; call start_vehicle(); confirm the same Engine now reports running == True.
# •	Stop the Car and confirm the Engine reports running == False.
# •	Create a Motorcycle with a separate Engine and verify its state is independent.
# •	Confirm Car and Motorcycle both inherit brand/model behavior from Vehicle.
# •	Confirm each subclass keeps its own additional state (doors / has_sidecar).
# •	Call service_vehicle(car) and service_vehicle(motorcycle); verify different messages without type branching.
# •	Call Vehicle.get_service_message() on a plain Vehicle and verify the base implementation.
# •	Explain exactly why print(car.start_vehicle()) may print None if the underlying start methods only mutate state.
# 8.6 Design questions before coding
# •	Why should Engine be composed into Vehicle instead of inherited by Vehicle?
# •	Why are Car and Motorcycle reasonable Vehicle subclasses?
# •	Where should engine running state live, and why should Vehicle not duplicate it?
# •	Which methods demonstrate delegation?
# •	Which methods demonstrate overriding?
# •	What behavior contract does service_vehicle() depend on?
# •	Could an unrelated object participate in service_vehicle() if it provides a compatible get_service_message()? Explain.
# •	Which future change would composition make easier—for example replacing Engine with another engine implementation?
# 8.7 Optional stretch - only after the required model works
# •	Add ElectricEngine with the same start/stop behavior and pass it into Vehicle without changing Vehicle.
# •	Create a list of different vehicle objects and loop over them, calling service_vehicle() for each.
# •	Add simple validation for blank brand/model only if it does not distract from the relationship concepts.
# Do not stretch into Day 3
# Do not add __repr__, __str__, __eq__, dataclasses, abstract base classes, or elaborate type hierarchies. Day 3 is where dunder methods + dataclasses receive focused attention.



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






