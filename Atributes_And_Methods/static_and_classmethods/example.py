class Car:
    # Class attribute
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    # Instance method
    def display(self):
        return f"{self.make} {self.model}"

    # Class method
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    # Static method
    @staticmethod
    def is_motor_vehicle():
        return True

# Creating instances of Car
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")
car3 = Car("Bmw","M5")
# Accessing instance method
print(car1.display())  # Output: Toyota Camry
print(car2.display())  # Output: Honda Accord
print(car3.display())  # Output: Bmw M5

# Accessing class method
print(Car.get_total_cars())  # Output: 3

# Accessing static method
print(Car.is_motor_vehicle())  # Output: True
