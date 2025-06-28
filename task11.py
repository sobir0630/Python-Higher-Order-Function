numbers = list(range(1, 21))

even_numbers = list(map(lambda x: x**2, filter(lambda y: y % 2 == 0, numbers)))
print(even_numbers)