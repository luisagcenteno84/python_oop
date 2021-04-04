from car import *

my_car = Car("yellow", "beetle", "1967")
my_other_car = Car("red", "corvette", "1999")

print(f"My car is: {my_car.color}")
print(f"It has {my_car.wheels} wheels")


my_car._cupholders = 8

print(f"It has {my_car._Car__cupholders} cupholders")

