#%%
print('hello luis')
# %%
import requests

response = requests.get('http://google.com')

response
# %%
import car
my_car = car.Car("yellow","beetle","1967")

print(f"My car is {my_car.color}")
# %%

print(f"Wheels: {my_car.wheels}")
# %%
