""" 
def list_avg(sequence):
    return sum(sequence) / len(sequence)

list_avg(123)
# OUTPUT
# TypeError: 'int' object is not iterable
 """
""" 
# In the above example, we encountered an error, however, it is hard to understand this while coding. Therefore, we can specify
# that the parameter must be a list and that the function will have a return value of float.

def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

# Recommended action
from typing import List
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)
 """

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book": #This is how you signal that these methods return an object of the same type 
        # that you're currently in. You can't do 
        # def hardcover(cls, name: str, page_weight: int) -> Book:
        # because this method is created before the class has finished processing.
        # If it returned a different class, then you would type the object name without the quotations.
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

