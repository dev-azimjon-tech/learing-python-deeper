import unittest
#Tasks for unittest
# Task 1, Add function test
# def add(a,b):
#     return a + b

# class TestAddFunc(unittest.TestCase):

#     def test_positive(self):
#         self.assertEqual(add(2, 2), 4)

#     def test_negative(self):
#         self.assertEqual(add(-1, -5), -6)

#     def test_zero(self):
#         self.assertEqual(add(0, 6), 6)


# # Task 2, Is Even:
# def is_even(n):
#     return n % 2 == 0


# class TestIsEven(unittest.TestCase):

#     def test_even(self):
#         self.assertTrue(is_even(10))

#     def test_odd(self):
#         self.assertFalse(is_even(9))

#     def test_zero(self):
#         self.assertTrue(is_even(0))


# # Task 3,Devide Function:
# def divide(a ,b):
#     return a / b

# class TestDivide(unittest.TestCase):

#     def test_divide(self):
#         self.assertEqual(divide(6, 2), 3)

#     def test_error(self):
#         self.assertRaises(divide(5, 0))



# # Task 4, Skip test Example
# def subtract(a, b):
#     return a - b 

# class TestExampleSubtract(unittest.TestCase):
    
#     @unittest.skip("Not ready yet")
#     def test_not_works(self):
#         self.assertEqual(subtract(3 ,2), 1)

#     def test_real(self):
#         self.assertEqual(subtract(10, 5) ,5)

# # Task 5, Capitalazi first latter
# def capitalize_first(s):
#     return s.capitalize()

# class TestCapitalize(unittest.TestCase):

#     def normal_test(self):
#         self.assertEqual(capitalize_first("hello"), "Hello")

#     def empty_test(self):
#         self.assertEqual(capitalize_first(""), "")

#     @unittest.skipIf(len("word") > 3, "Too long")
#     def long_test(self):
#         self.assertEqual(capitalize_first("world"), "World") 

# Task 1, Math Test
# def addition(a,b):
#     return a + b

# def subtraction(a,b):
#     return a - b 

# def multiplication(a,b):
#     return a * b

# def division(a,b):
#     return a / b

# class TestMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(addition(10, 20), 30)

#     def test_substract(self):
#         self.assertEqual(subtraction(5, 2), 3)

#     def test_multiply(self):
#         self.assertEqual(multiplication(2, 2), 4)

#     def test_divide(self):
#         self.assertEqual(division(10, 2), 5)

if __name__ == "__main__":
    unittest.main()