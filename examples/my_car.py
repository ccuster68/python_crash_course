from car import Car

my_new_car = Car('Audi', 'a4', 2019)

print(f'{my_new_car.get_descriptive_name()}')

my_new_car.odometer_reading=23
my_new_car.read_odometer()