class Car:
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.motor_reading = 450

    def get_descriptive_name(self):
        long_name = f"\t{self.year} {self.make} {self.model}"
        return long_name

    def read_meter(self):
        print(f"\tThis car has {self.motor_reading} kilometers on it.")

    def fill_gas_tank(self):
        print("\tFilling gas tank!")

    def update_meter(self, mileage):
        if mileage >= self.motor_reading:
            self.motor_reading = mileage
        else:
            print("\tYou can't roll back the meter!")

    def increment_meter(self, miles):
        self.motor_reading += miles


class Battery:
    def __init__(self, description, battery_size):
        self.description = description
        self.battery_size = battery_size

    def print_details(self):
        print(f"\tBattery size is {self.battery_size}kwh")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"\tThis car has a {range}km range")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"\tUpgrading battery size to 100kw")
        elif self.battery_size == 100:
            print(f"\tBattery size already 100kwh")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery('A juicy battery!', 75)

    def fill_gas_tank(self):
        print("\tElectric cars don't have gas tanks...")


# my_new_car = Car('audi', 'a4', 2019)
# my_new_car.fill_gas_tank()
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.print_details()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.print_details()
my_tesla.battery.get_range()