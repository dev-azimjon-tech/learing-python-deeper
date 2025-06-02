# Task 1
# class Math:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     def substraction(a,b):
#         return a - b
#     def multiple(a,b):
#         return a * b
#     def devision(a,b):
#         return a / b

# print(Math.add(10, 20))
# print(Math.substraction(10, 20))
# print(Math.multiple(10, 20))
# print(Math.devision(10, 20))

# Task 2
# class StringHelper:
#     @staticmethod
#     def is_palindrome(string):
#         if string == string[::-1]:
#             return "String Is Palindrome"
#         else:
#             return "String Is Not Palindrome"

#     @staticmethod
#     def reverse_string(s):
#         if s == "":
#             return s
#         else:
            
#             return s[::-1]

#     @staticmethod
#     def count_sentence(sentence):
#         return len(sentence.split())

# # Test calls
# print(StringHelper.is_palindrome("madam"))
# print(StringHelper.is_palindrome("hello"))
# print(StringHelper.reverse_string("Hello World"))
# print(StringHelper.count_sentence("Python is fun to learn"))

# Task 3
# class PasswordUtils:
#     @staticmethod
#     def is_strong(password):
#         if len(password) < 8:
#             return False
        
#         has_digit = any(char.isdigit() for char in password)
#         has_upper = any(char.isupper() for char in password)
        
#         return has_digit and has_upper


# print(PasswordUtils.is_strong("Password123"))
# print(PasswordUtils.is_strong("password"))
# print(PasswordUtils.is_strong("PASSWORD"))
# print(PasswordUtils.is_strong("Pass12"))

        