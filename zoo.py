
import random

class Animal:
    def __init__(self,species,name, age, health, hunger, happiness):
        super().__init__()
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
    def grow(self):
        self.age += 1
        self.health = random.randint(0,10)
        self.hunger = random.randint(0,10)
        self.happiness = random.randint(0,10)
    def eat(self):
        if self.hunger >= 6:
            self.health += random.randint(0, 5)
            self.happiness += random.randint(0, 5)
            self.hunger -= random.randint(5, 10)
        else:
            print({self.name} , "hungry")
    def play(self):
        pass #happiness ....
class Zoo:
    def __init__(self):
        super().__init__()
        self.animals = []

#ДОПИСАТИИИИ !