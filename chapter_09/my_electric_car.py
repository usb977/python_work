from car import Car
from electric_car import ElectricCar

my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
my_new_car.update_odometer(25)
my_new_car.read_odometer()

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()