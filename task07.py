prices = ["$120", "$340", "$50", "$90"]

new_price = list(map(lambda price: price.replace('$', ''), prices))

print(new_price)