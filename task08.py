people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]
new_people = sorted(people, key=lambda person: person["age"], reverse=False)
print(new_people)