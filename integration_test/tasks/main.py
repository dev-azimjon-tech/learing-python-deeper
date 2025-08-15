# Task 1
# cart = []

# def add_to_cart(item, price):
#     cart.append({"item": item, "price": price})

# def calculate_total():
#     return sum(product["price"] for product in cart)

# def checkout(discount=0):
#     total = calculate_total()
#     return total - (total * discount)


# add_to_cart("Apple", 1)
# add_to_cart("Banana", 2)
# print("Total with 10% discount:", checkout(0.1))

# Task 2:

library = []

def add_book(title):
    library.append({"title": title, "available": True})

def borrow_book(title):
    for book in library:
        if book["title"] == title and book["available"]:
            book["available"] = False
            return True
    return False

def search_book(title):
    return any(book["title"] == title for book in library)


add_book("Python 101")
borrow_book("Python 101")
print("Book available after borrow?", search_book("Python 101"))
