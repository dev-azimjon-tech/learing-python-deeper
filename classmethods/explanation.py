class MyClass:
    count = 0

    def __init__(self, name):
        self.name = name
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Creating instances of MyClass
obj1 = MyClass("John")
obj2 = MyClass("Doe")

# Accessing class method
print(MyClass.get_count())  # Output: 2


class Library:
    books_count = 0

    def __init__(self):
        Library.books_count += 1

    @classmethod
    def total_books(cls):
        return f"Total books: {cls.books_count}"

# Create books
b1 = Library()
b2 = Library()
b3 = Library()

print(Library.total_books())  # Output: Total books: 3


class Student:
    school_name = "Tajik High School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def from_string(cls, student_str):
        name, grade = student_str.split("-")
        return cls(name, grade)

# Creating object using class method
student1 = Student.from_string("Azimjon-9th")
print(student1.name)   # Output: Azimjon
print(student1.grade)  # Output: 9th
