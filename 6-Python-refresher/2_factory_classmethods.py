class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book({self.name!r}, {self.book_type!r}, {self.weight!r})>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)

book = Book("Sherlock Holmes", "hardcover", 1500)
print(f"{book.name}, {book.book_type}, {book.weight}")
print(book, end="\n\n")

book2 = Book.hardcover("Atomic Habits", 885)
print(book2)

book3 = Book.paperback("Python 101", 675)
print(book3)
