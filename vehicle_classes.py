"""
Name: Vehicle Classes
Author: Tyke Anfield
Date: 11-8-2022
Purpose: The app will store user input into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes above.
The app will then output the data in an easy-to-read and understandable format.
"""

class Vehicle:
  def __init__(self, type):
    self.type = type

type = input("Enter vehicle type: ")

class Automobile(Vehicle):
  def __init__(self, type, year, make, model, doors, roof):
    super().__init__(type)
    self.year = year
    self.make = make
    self.model = model
    self.doors = doors
    self.roof = roof

year = int(input(f"Enter the year {type} was made: "))
make = input(f"Enter the make of {type}: ")
model = input(f"Enter the model of  {type}: ")
doors = int(input(f"Enter the number of doors {type} has: "))
roof = input(f"Enter the roof type 'solid or sun roof' {type} has: ")

while roof != "solid" or "sun roof":
  if roof == "solid":
    break
  elif roof == "sun roof":
    break
  else:
    roof = input(f"Enter the roof type 'solid or sun roof' {type} has: ")

user_Car = Automobile(type, year, make, model, doors, roof)
print("\n" "Vehicle type:", user_Car.type,  "\n"
     "Year:", user_Car.year, "\n"
      "Make:", user_Car.make.capitalize(), "\n"
      "Model:", user_Car.model.capitalize(), "\n"
      "Number of doors:", user_Car.doors, "\n"
      "Type of roof:", user_Car.roof, "\n"
     )


