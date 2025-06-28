sentence = "Functional programming in Python is very powerful and elegant"


words = sentence.split()
uzun_suz = sorted(words, key=len, reverse=True)[:3]
print(uzun_suz)