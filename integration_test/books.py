def get_book(book_id):
    books = {
        1:{"title":"1984", "available":True},
        2:{"title":"Dune", "available":False}
    }
    return books.get(book_id)

def mark_as_borrowed(book_id):
    # Pretend this updates DB
    return True
