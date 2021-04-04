import requests
import car

print('hello luis')
# %%

response = requests.get('http://google.com')

response
# %%
my_car = car.Car("yellow", "beetle", "1967")

print(f"My car is {my_car.color}")
# %%

print(f"Wheels: {my_car.wheels}")
