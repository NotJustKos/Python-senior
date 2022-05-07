from unicodedata import name


class Good:
    print("Hi!")
    def _init_(self,name,age):
        self.name = name
        self.age = age
        print("i'm alive!")

first_good = Good(name="Clyde",age=23)
print(first_good.name)
print(first_good.age)

second_good = Good(name="Kathrine",age=30)
print(second_good.name)
print(second_good.age)


class Evil:
    print("Hi!")
    def _init_(self,name,age):
        self.name = name
        self.age = age
        print("i'm alive!")

first_evil = Evil(name="Ben",age=28)
print(first_evil.name)
print(first_evil.age)

second_evil = Evil(name="Kate",age=20)
print(second_evil.name)
print(second_evil.age)