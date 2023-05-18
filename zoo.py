
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
        if self.happiness >= 5:
            self.health += random.randint(0,5)
            self.hunger += random.randint(0, 5)
            self.happiness += random.randint(0, 5)
        else:
            print({self.name} , "doesn't wanna play" )
    def __str__(self):
        return f"{self.species} - {self.name} ({self.age} years old\n"
               f"Health: {self.health}\n Hunger: {self.hunger}\n Happiness : {self.happiness}\n"


class Zoo:
    def __init__(self):
        super().__init__()
        self.animals = []
    def add_animal(self,animal):
        self.animals.append(animal)
    def remove_animal(self,animal):
        if animal in self.animals:
            self.animals.remove(animal)
    def feed_all(self):
        for animal in self.animals:
            animal.eat()
    def play_with(self,animal):
        if animal in self.animals:
            animal.play()
    def grow_all(self,animal):
        for animal in self.animals:
            animal.grow()
    def __str__(self):
        return "\n".join([str(animal) for animals in self.animals])


def zoo_state(zoo,day):
    filename = f"Day_{day}.txt"
    with open (filename, "w") as file:
        file.write(str(zoo))

zoo = Zoo()

zoo.add_animal("Elephant" , "Ronnie" , 16 , 2 , 3 , 5)
zoo.add_animal("Tiger" , "David" , 24 , 6 , 8 , 4)
zoo.add_animal("Crocodile" , "Chris" , 4 , 10 , 6 , 9)

for i in range(1,11):
    print(f"\Day {i}")
    zoo_state(zoo,i)
    zoo.feed_all()
    zoo.play_with(zoo.animals[random.randint(0, len(zoo.animals) - 1)])
    zoo.grow_all()
    print(zoo)
    print("\n")

print("That's all")