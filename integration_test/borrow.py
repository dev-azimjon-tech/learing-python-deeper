from books import get_book, mark_as_borrowed
from users import get_user

def borrow_book(user_id,book_id):
    user = get_user(user_id)
    book = get_book(book_id)

    if not user or not book:
        return "User or book not found "
    if not book["available"]:
        return "Book not available"
    
    mark_as_borrowed(book_id)
    return f"{user["name"]} borrowed {book["title"]}"