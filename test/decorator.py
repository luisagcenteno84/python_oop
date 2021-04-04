from car import *
my_car = Car("yellow", "beetle", "1967")

print(f"My car uses {my_car.voltage} volts")

my_car.voltage = 6

print(f"My car now uses {my_car.voltage} volts")

del my_car.voltage