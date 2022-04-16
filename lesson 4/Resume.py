from unicodedata import name

name = input("Ваше ім'я")

lastname = input("Ваша фамілія")

age = input("Ваш вік")


Resume = "Ваше резюме," + name + lastname + age
print(Resume)
