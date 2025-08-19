""" 
class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Bookshelf with {self.quantity} books."

#Composition is a counterpart to inheritance to build out classes that use other classes.

shelf = BookShelf(300)
print(shelf)
        

class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter", 120)
print(book)
 """

# In the above example, Book is inherited from BookShelf. Book does not need the quantity attribute, but it still has to keep it
# Similarly, Book has to create its __str__ method just because the BookShelf __str__ method is not useful for Book.
# Composition comes into play over here. Inheritance is not required to relate classes.

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

class Book():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book1 = Book("Python 101")
shelf = BookShelf(book, book1)

print(shelf)
print(shelf.books)