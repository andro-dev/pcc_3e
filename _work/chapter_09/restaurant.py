class Restaurant:
    def __init__(self, name, cuisine_type, number_served=0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number):
        while True:
            if number > 0:
                self.number_served += number
                break
            else:
                number = int(
                    input(
                        f"Please enter number to increase 'Number Served' \nfor {self.name} restaurant: \n--> "
                    )
                )
                continue

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


r1 = Restaurant("Sushi World", "Japanese")
r2 = Restaurant("Taco Town", "Mexican")

r1.number_served = 100
print(f"{r1.name} number served:", r1.number_served)

r2.number_served = 25
print(f"{r2.name} number served:", r2.number_served)

print()
r1.increment_number_served(500)
r2.increment_number_served(-20)

print(f"{r2.name} number served:", r2.number_served)
print(f"{r1.name} number served:", r1.number_served)
