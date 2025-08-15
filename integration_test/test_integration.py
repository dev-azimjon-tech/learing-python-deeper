from borrow import borrow_book

def test_borrow_book_succes():
    result = borrow_book(1, 1)
    assert result == "Alice borrowed 1984"

def test_borrow_book_unavailable():
    result = borrow_book(1, 2)  
    assert result == "Book not available"