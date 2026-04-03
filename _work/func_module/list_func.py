

def create_list_of_random_numbers(number_of_items: int, start:int, stop:int):
    import random
    return [random.randint(start, stop) for n in range(number_of_items)]


print(create_list_of_random_numbers(5, 100, 200))
print(create_list_of_random_numbers(10, 100, 1000))
