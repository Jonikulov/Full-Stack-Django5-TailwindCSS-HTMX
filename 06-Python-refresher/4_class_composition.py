class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"

    def __repr__(self):
        return f"<Book({self.name!r})>"


book = Book("Python 201")
book2 = Book("Django Master")
shelf = BookShelf(book, book2)

print(book)
print(book2)
print(shelf)
print(shelf.books)
