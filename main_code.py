from datetime import datetime

class Vehicle:
    vehicle_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Vehicle.vehicle_count += 1

    def start_engine(self):
        # Polymorphic method (overridden in child classes)
        return f"{self.brand} {self.model}'s engine started."

    @classmethod
    def get_vehicle_count(cls):
        return f"Total vehicles: {cls.vehicle_count}"

    @staticmethod
    def is_valid_year(year):
        current_year = datetime.now().year
        return 1886 <= year <= current_year


# Child class 1
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def start_engine(self):
        return f"{self.brand} {self.model} roars to life with {self.doors} doors."


# Child class 2
class Motorcycle(Vehicle):
    def __init__(self, brand, model, helmet_required=True):
        super().__init__(brand, model)
        self.helmet_required = helmet_required

    def start_engine(self):
        return f"{self.brand} {self.model} revs its engine. Helmet required: {self.helmet_required}"



car = Car("Toyota", "Camry", 4)
bike = Motorcycle("Yamaha", "R3")

for vehicle in [car, bike]:
    print(vehicle.start_engine())


print(Vehicle.get_vehicle_count())
print("Is 2023 a valid vehicle year?", Vehicle.is_valid_year(2023))
print("Is 1700 a valid vehicle year?", Vehicle.is_valid_year(1700))
