from unicodedata import name

names = input("Ваше ім'я")

lastname = input("Ваша фамілія")

age = input("Ваш вік")

country = input("Ваша країна")

city = input("Ваш город")

ilnesses = input("У вас э хвороби")

height = input("Ваш зріст")

settlement = input("Ваш дім")

Resume = "Ваше резюме," + names + lastname + age + country + city + ilnesses + height + settlement
print(Resume)
