import random
from turtle import home


class Human:
    def _init_(self,name = "Human",job = None, Home = None, Car = None):
        self.name = name
        self.money = 100
        self.gledness = 50
        self.setiety = 50
        self.job = job
        self.home = Home
        self.car = Car

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass
    
    def eat(self):
        pass
    
    def work(self):
        pass

    def shopping(self,mange):
        pass
    
    def chill(self):
        pass

    def clean_home(self):
        pass

    def days_index(self,day):
        pass

    def is_alive(self):
        pass

    def live(self,day):
        pass

    class Auto:
        def __init__(self,brand_list):
            self.brand = random.choice(list(brand_list))
            self,color = brand_list[self.brand]["color"]
    class House:
    def _init_(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

brands_of_car = {
    "BMV": {"color":"Black"},
    "Lada": {"color":"gray"},
    "BMV": {"color":"yellow"},
    "Ferrari": {"color":"blue",}
}

job_list = {
    "Python Developer": {"salary":40,"gladness_less":3},
    "Teacher": {"salary":25,"gladness_less":25},
    "Python Developer": {"salary":40,"gladness_less":30},
    "Taxi Driver": {"salary":20,"gladness_less":15},
    "Manager": {"salary":30,"gladness_less":20}, 
}