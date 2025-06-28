votes = [
    {"option": "A", "votes": 123},
    {"option": "B", "votes": 145},
    {"option": "C", "votes": 97}
]

max_votes = max(votes, key=lambda x: x["votes"])

print(max_votes)
