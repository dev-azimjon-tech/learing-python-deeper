# # Task 1
# class Shape:
#     def area(self):
#         raise NotImplementedError("Message that should be in base classes")

# class Circle(Shape):
#     circle_c = 0
#     def __init__(self, radius):
#         self.radius = radius
#         Circle.circle_c += 1
#     def area(self):
#         return f"Area of Circle: {3.14*self.radius**2}"


#     @classmethod
#     def circle_counter(cls):
#         return f"Circles are: {cls.circle_c}"
    
#     @staticmethod
#     def info_circle(info_about_circle):
#         return info_about_circle

# class Square(Shape):
#     square_s = 0

#     def __init__(self, side):
#         self.side = side
#         Square.square_s += 1

#     def area(self):
#         return f"Area of Squeare :{self.side **2}"
    
#     @classmethod
#     def square_counter(cls):
#         return f"Squares are {cls.square_s}"

#     @staticmethod
#     def info_square(info_about_square):
#         return info_about_square
    

# circle = Circle(21)
# square = Square(41)

# print(Circle.info_circle("Some info about Circle"))
# print(Circle.circle_counter())
# print(circle.area())

# print(Square.info_square("Some Info about Square"))
# print(Square.square_counter())
# print(square.area())


# # Task 2
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def describe(self):
#         raise NotImplementedError("Should be in base classes")

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self.grade = grade

#     def describe(self):
#         return f"This student is in: {self.grade} grade, his name is: {self.name} and he is: {self.age} years old"

#     @classmethod
#     def from_string(cls, student_string, grade):
#         name, age = student_string.split(" - ")
#         return cls(name, int(age), grade)

#     @staticmethod
#     def validate(age):
#         if age >= 5:
#             return "The valid age for school"
#         else:
#             return "The age is not valid for school"

# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def describe(self):
#         return f"This teacher teaches: {self.subject}, his name is: {self.name} and he is: {self.age} years old"

#     @classmethod
#     def from_string_teacher(cls, teacher_string, subject):
#         name, age = teacher_string.split(" - ")
#         return cls(name, int(age), subject)


# student = Student.from_string("Azimjon - 16", 9)
# teacher = Teacher.from_string_teacher("Olim Aka - 60", "Math")


# print(student.describe())
# print(Student.validate(16))
# print(teacher.describe())



# Task 3
# class Vehicle:
#     def __init__(self, name, speed, weight):
#         self.name = name
#         self.speed = speed
#         self.weight = weight

#     def display_info(self):
#         raise NotImplementedError("This function should be in base class")

#     @staticmethod
#     def kmh_to_mph(kmh):
#         return f"Speed in MPH is: {0.6214 * kmh:.2f}"

# class Car(Vehicle):
#     def display_info(self):
#         return f"This car is: {self.name}, speed: {self.speed} km/h, weight: {self.weight} kg"

# class Motorcycle(Vehicle):
#     def display_info(self):
#         return f"This motorcycle is: {self.name}, speed: {self.speed} km/h, weight: {self.weight} kg"

# class Truck(Vehicle):
#     def display_info(self):
#         return f"This truck is: {self.name}, speed: {self.speed} km/h, weight: {self.weight} kg"


# car = Car("BMW", 200, 1000)
# motorcycle = Motorcycle("Yamaha", 180, 200)
# truck = Truck("Volkswagen", 100, 10000)


# for vehicle in [car, motorcycle, truck]:
#     print(vehicle.display_info())

# print(Vehicle.kmh_to_mph(200))


# Task 4
# class FoodItem:
#     def __init__(self, name : str, price : int) -> None:
#         self.name : str = name
#         self.price : int = price
    
#     def prepare(self) -> str:
#         return f"Food: {self.name} and it's price: {self.price}"

# class Pizza(FoodItem):
#     def __init__(self, name, price):
#         super().__init__(name, price)

#     def prepare(self):
#         return super().prepare()
    
# class Burger(FoodItem):
#     def __init__(self, name, price):
#         super().__init__(name, price)

#     def prepare(self):
#         return super().prepare()
    
# class Salad(FoodItem):
#     def __init__(self, name, price):
#         super().__init__(name, price)

#     def prepare(self):
#         return super().prepare()

# pizza = Pizza("Pizaa", 200)
# burger = Burger("Burger",160)
# salad = Salad("Salad", 90)

# print(pizza.prepare())
# print(burger.prepare())
# print(salad.prepare())

# Task 5
# class Room:
#     def __init__(self, room_number : int, price_per_knight : int) -> None:
#         self.room_number : int = room_number
#         self.price_per_knight : int = price_per_knight

#     def get_details(self):
#         return f"Room number: {self.room_number}, and price for per knight: {self.price_per_knight}"
    

# class SingleRoom(Room):
#     def __init__(self, room_number, price_per_knight, has_tv):
#         super().__init__(room_number, price_per_knight)
#         self.has_tv = has_tv

#     def get_details(self):
#         return f"{super().get_details()} And it has: {self.has_tv}"

# class DoubleRoom(Room):
#     def __init__(self, room_number, price_per_knight, has_balcony):
#         super().__init__(room_number, price_per_knight)
#         self.has_balcony = has_balcony

#     def get_details(self):
#         return f"{super().get_details()} And it has: {self.has_balcony}"
        

# singleroom = SingleRoom(2312, 100, "Tv")
# doubleroom = DoubleRoom(321, 200, "Balcony")

# print(singleroom.get_details())
# print(doubleroom.get_details())

