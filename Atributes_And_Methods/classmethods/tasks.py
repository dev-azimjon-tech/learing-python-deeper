# #Task 1
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     @classmethod
#     def from_string(cls, book_string):
#         title, author = book_string.split(" - ")
#         return cls(title, author)

#     def display_info(self):
#         return f"Title: {self.title}, Author: {self.author}"



# book1 = Book("1984", "George Orwell")
# book2 = Book.from_string("Harry Potter - J.K. Rowling")
# print(book1.display_info())
# print(book2.display_info())

# #Task 2
# class Student:
#     students = 0

#     def __init__(self,name_student):
#         self.name_student = name_student
#         Student.students += 1

#     @classmethod
#     def count_all_studets(cls):
#         return cls.students
    
# s1 = Student("Aza")
# s2 = Student("Aza2")

# print(Student.count_all_studets())

# #Task 3
# class App:
#     version = "1.0.0"

#     @classmethod
#     def show_version(cls):
#         print(f"App Version: {cls.version}")

# App.show_version()

# #Task 4
# class Person:
#     @classmethod
#     def get_category_by_age(cls, age):
#         if age < 0:
#             return "Invalid age"
#         elif age < 13:
#             return "Child"
#         elif age < 18:
#             return "Teen"
#         else:
#             return "Adult"


# print(Person.get_category_by_age(7))
# print(Person.get_category_by_age(15))
# print(Person.get_category_by_age(25))
# print(Person.get_category_by_age(-3))
