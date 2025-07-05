import unittest


# def add(a,b):
#     return a + b

# class TestAddFunction(unittest.TestCase):

#     def test_positive_nums(self):
#         self.assertEqual(add(2, 3), 5)

#     def test_negative_nums(self):
#         self.assertEqual(add(-1, -1), -2)
    
#     def test_zero_num(self):
#         self.assertEqual(add(0, 5), 5)


# Unittest @skip:
# Example 1:
class TesteExample(unittest.TestCase):

    @unittest.skip("Not ready yet")
    def test_feature_in_development(self):
        self.assertEqual(1, 2)

    @unittest.skipIf(True, "Condition met, skipping")
    def test_skip_conditionaly(self):
        self.assertEqual(2, 2)

# Example 2:

class TestMath(unittest.TestCase):

    @unittest.skip("This is not ready")
    def test_divide(self):
        self.assertEqual(5 - 3, 2)

    def test_plus(self):
        self.assertEqual(5 + 2, 7)

# Example 3:

class TestExample(unittest.TestCase):

    @unittest.skipIf(5 > 3, "Will skip this test because 5 > 3")
    def test_should_skip(self):
        self.assertEqual(1, 1)

    def test_should_runt(self):
        self.assertEqual(2, 2)


# Example 4:

class TestExample1(unittest.TestCase):
    @unittest.skipUnless(2 + 2 == 4,"Runs only when math is correct")
    def test_basic_math(self):
        self.assertEqual(2 + 2, 4)




if __name__ == "__main__":
    unittest.main()