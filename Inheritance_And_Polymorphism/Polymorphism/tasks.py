# Task 1
# class Shape:
#     def calculate_area(self):
#         raise NotImplementedError("This function should be called")
    
# class Circle(Shape):
#     def __init__(self, p : float, r : int) -> None:
#         self.p : float = p
#         self.r : int = r 
#     def calculate_area(self):
#         return self.p*self.r**2

# class Rectangle(Shape):
#     def __init__(self, length : int, height: int) -> None:
#         self.length : int = length
#         self.height : int = height
        
#     def calculate_area(self):
#         return self.length * self.height

# class Triangle(Shape):
#     def __init__(self, base : int, heigth : int) -> None:
#         self.base : int = base
#         self.heigth : int = heigth
        
#     def calculate_area(self):
#         return 0.5*self.base*self.heigth

# def calculate_areas(shape):
#     print(shape.calculate_area())        

# circle = Circle(3.14, 41)
# rectangle = Rectangle(34, 65)
# triangle = Triangle(412, 903)

# print(circle.calculate_area())
# print(rectangle.calculate_area())
# print(triangle.calculate_area())

# Task 2
# Базовый класс (родительский)
# class PaymentMethod:
#     def process_payment(self, amount):
#         raise NotImplementedError("Метод должен быть переопределён в подклассе")

# # Подкласс: Кредитная карта
# class CreditCardPayment(PaymentMethod):
#     def process_payment(self, amount):
#         print(f"[CreditCard] Платёж на сумму {amount}$ обработан.")

# # Подкласс: PayPal
# class PayPalPayment(PaymentMethod):
#     def process_payment(self, amount):
#         print(f"[PayPal] Платёж на сумму {amount}$ обработан.")

# # Подкласс: Банковский перевод
# class BankTransferPayment(PaymentMethod):
#     def process_payment(self, amount):
#         print(f"[BankTransfer] Платёж на сумму {amount}$ обработан.")

# # Полиморфная функция обработки платежа
# def process_any_payment(payment_method: PaymentMethod, amount: float):
#     payment_method.process_payment(amount)


#     payments = [
#         CreditCardPayment(),
#         PayPalPayment(),
#         BankTransferPayment()
#     ]


#     for payment in payments:
#         process_any_payment(payment, 99.99)
