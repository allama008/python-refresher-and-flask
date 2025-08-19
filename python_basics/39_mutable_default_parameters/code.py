""" 
from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = []): # This is bad!
        # Never make a parameter equal to a mutable value by default.
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)
        
rolf = Student("Rolf")
print(rolf.grades)
 """
# OUTPUT
# [90]
# [90]

# Rolf did not take the exam, yet, he also has 90 in his grades, this is why setting an empty list as default value is a bad idea.
# The function parameters (these default ones) evaluate when the function is defined, not when the function is called.

# When the class is created, the functions are evaluated so that Python knows what the parameters are and what the name is and so on.
# The self.grades refers to the empty list created in function definition. 
# Therefore, self.grades points to the same list for both Bob and Rolf.
# If you pass your own list, then it won't use the default list and it will seem like the problem is resolved, however, still, if two
# or more students do not pass any list, then those objects will share the default list.

""" 
from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = None): # Passing None here.
        self.name = name
        self.grades = grades or [] # If None is default value, then None or empty list will evaluate to empty list.

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)
        
rolf = Student("Rolf")
print(rolf.grades)
 """

from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None): # Slightly better way of handling it, so that Python knows
        # that it may not be a list initially, it may be None, but you're going to set it to a list later on.
        self.name = name
        self.grades = grades or [] # If None is default value, then None or empty list will evaluate to empty list.

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)
        
rolf = Student("Rolf")
print(rolf.grades)

# Use immutable data types and if you have to use mutable data types, then follow the pattern used above.