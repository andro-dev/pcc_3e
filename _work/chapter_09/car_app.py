import sys
from car import Car, ElectricCar


def run(section):
    print("inside function:", sys._getframe().f_code.co_name) # get current functon name inside the function
    if section == "car":
        #######################################################################
        #   Car Section
        #######################################################################
        car1 = Car("subaru", "forrester", 2017)
        print(car1.get_descriptive_name())
        # car1.read_odometer()

        car1.odometer_reading = 82_823
        car1.read_odometer()

        car2 = Car("bmw", "325 M3", 2009)
        car2.get_descriptive_name()
        # print(vars(car2))

        car2.update_odometer(50_000)
        car2.read_odometer()

        car2.increment_odometer(100_000)
        car2.read_odometer()

        car2.fuel__tank_capacity = 20
        car2.fill_gas_tank(30)
        print(vars(car2))

        #######################################################################
        #   Electric Car Section
        #######################################################################
    elif section == "electric":
        tesla1 = ElectricCar("tesla", "model s", 2026)
        print(tesla1.get_descriptive_name())
        tesla1.battery.describe_battery()


def main():
    pass
    # run(section='car')
    # run(section='electric')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file, *sections = sys.argv
        [run(section) for section in sections]
    # main()

run("hello")
