students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

sorted_studints = sorted(students, key=lambda x: x["grade"])
print(sorted_studints)