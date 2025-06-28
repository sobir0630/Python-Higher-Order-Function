
data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = [item for item in data if isinstance(item, str) and len(item) > 5]
print(result)