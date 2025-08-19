""" 
class ClassTest:
    def instance_method(self): #All functions inside the class that use the object as a first parameter are called instance methods.
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls): #When @classmethod is put at the top, then cls will be the class itself.
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static method")


test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
# OUTPUT
# Called instance_method of <__main__.ClassTest object at 0x102956ba0>
# Called instance_method of <__main__.ClassTest object at 0x102956ba0>

ClassTest.class_method() # When you don't pass anything to the class_method function, then python will ClassTest as a parameter.
# ClassTest.class_method(ClassTest)
# OUTPUT
# Called class_method of <class '__main__.ClassTest'>

ClassTest.static_method() # Not really a method because it does not have any information about the class or object. Works a simple separate function.
 """

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    # Currently there is no mechanism to restrict the object's book type to hardcover or paperback.
    # If you pass a value such as 'comic book' as the book type, it will assign it to the object.
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100) # return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight) # return cls(name, cls.TYPES[1], page_weight)
""" 
print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)
print(book.name)

print(book)
 """

book = Book.hardcover("Harry Potter", 1500)
print(book)

light = Book.paperback("Python 101", 600)
print(light)