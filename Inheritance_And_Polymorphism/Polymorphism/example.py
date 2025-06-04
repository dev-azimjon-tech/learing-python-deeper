# Polymorphism in Python
# Polymorphism is an OOP principle that allows objects of different classes to be treated asobjects of a common superclass. 
# It enables a single interface to represent different underlying forms (data types)

## Overview of Polymorphism

### Method Overriding

# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. 
# This allows the subclass to provide a specific behavior while maintaining a consistent interface.

class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!


### Polymorphism with Functions

# You can use polymorphism with functions to handle objects of different classes through a common interface.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def print_area(shape):
    print(f"The area is {shape.area()}")

circle = Circle(5)
square = Square(4)

print_area(circle)  # Output: The area is 78.5
print_area(square)  # Output: The area is 16
