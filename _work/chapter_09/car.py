class Car:
    def __init__(self, make, model, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel = 0
        self.fuel__tank_capacity = 30

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        self.odometer_reading = miles

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Your can't roll back an odometer")

    def fill_gas_tank(self, add_gallons):
        if self.fuel + add_gallons <= self.fuel__tank_capacity:
            self.fuel += add_gallons
        else:
            gallons_to_max = self.fuel__tank_capacity - self.fuel
            # self.fuel += gallons_to_max
            print(
                f"Put {gallons_to_max} to fill the tank to max. You're not charges for {add_gallons - gallons_to_max} gallons"
            )
            self.fill_gas_tank(gallons_to_max)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self):
        self.battery_size = 40

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")



