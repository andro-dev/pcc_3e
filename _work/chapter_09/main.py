from restaurant import Restaurant, IceCreamStand


restaurant = Restaurant("Matuba", "Japaneese Sushi")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"{restaurant.restaurant_name} before has served: {restaurant.number_served}")
restaurant.number_served = 250
print(f"{restaurant.restaurant_name} after has served: {restaurant.number_served}")

restaurant.set_number_served(500)
print(
    f"After methon call {restaurant.restaurant_name} has served:{restaurant.number_served}"
)

restaurant.increment_number_served(199)
print(
    f"{restaurant.restaurant_name} after increment has served: {restaurant.number_served}"
)

ics = IceCreamStand("Bethesda Ice Cream", "Ice Cream")
ics.describe_restaurant()
print(f"Flavors: {ics.display_flavors()}")
