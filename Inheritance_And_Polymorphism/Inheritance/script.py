# Inheritance in Python
# Inheritance is a fundamental concept in object-oriented programming (OOP)
# that allows a class (called a child class or subclass) to inherit attributes
# and methods from another class (called a parent class or superclass).
# This promotes code reuse and establishes a hierarchical relationship between classes.


### Defining a Parent Class

# A parent class contains attributes and methods that will be inherited by child classes:
# class Animal:
#     def __init__(self, name : str) -> None:
#         self.name : str = name

#     def speak(self) -> str:
#         raise NotImplementedError("Subclasses must implement this method")

### Creating a Child Class

# A child class inherits attributes and methods from the parent class.
# You define a child class by passing the parent class as an argument in the class definition:

# class Cat(Animal):
#     def speak(self) -> str:
#         return f"{self.name} says Meow!"

### Using `super()`

# The `super()` function allows you to call methods from the parent class within the child class.
#  This is often used to extend or modify the behavior of inherited methods.

# class Dog(Animal):
#     def __init__(self, name : str, breed : str) -> None:
#         super().__init__(name)
#         self.breed : str = breed

#     def speak(self) -> str:
#         return f"{self.name} the {self.breed} says Woof!"

# And the full example of Inheritance:

class Animal:
    def __init__(self, name : str) -> None:
        self.name : str = name

    def speak(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
