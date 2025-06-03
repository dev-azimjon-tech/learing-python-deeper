# Task 1
class Vehicle:
    def __init__(self, brand : str , year : int , color : str) -> None:
        self.brand : str = brand
        self.year : int = year
        self.color : str = color


class Car(Vehicle):
    def __init__(self, brand : str, year : int, color : str, number_of_wheel : int) -> None:
        super().__init__(brand, year, color)
        self.number_of_wheel : int = number_of_wheel
    def info(self) -> str:
        return f"Car brand: {self.brand} \n Year of car: {self.year} \n Color of car: {self.color} \n Car has: {self.number_of_wheel} wheels"

class Motorcycle(Vehicle):
    def info(self) -> str:
        return f"Motorcycle brand: {self.brand} \n Year of motorcycle: {self.year} \n Color of motorcycle: {self.color}"
    
class Truck(Vehicle):
    def info(self) -> str:
        return f"Truck brand: {self.brand} \n Year of truck: {self.year} \n Color of truck: {self.color}"

car = Car("Bmw", 2001, "Red", 4)
motorcycle = Motorcycle("Moto", 1999, "White")
truck = Truck("Volwo", 2000, "Gray")

print(car.info())
print(motorcycle.info())
print(truck.info())

# Task 2
class Animal:
    def __init__(self, voice : str) -> None:
        self.voice : str = voice

class Cow(Animal):
    def make_sound(self) -> str:
        return f"Cow says: {self.voice}"

class Duck(Animal):
    def make_sound(self) -> str:
        return f"Duck says: {self.voice}"

class Sheep(Animal):
    def make_sound(self) -> str:
        return f"Sheep says: {self.voice}"

cow = Cow("Moo")
duck = Duck("Gaaa")
sheep = Sheep("Baa")

print(cow.make_sound())
print(duck.make_sound())
print(sheep.make_sound())