emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

gmail = list(filter(lambda email: email.endswith("@gmail.com"), emails))
print(gmail)

