""" 
student = {"name": "Rolf", "grades":(89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))
 """
""" 
class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (89, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student.name)
print(student.grades)


# __init__ method is a special "dunder" method that serves as the constructor for a class. Primary purpose
# is to initialize the attributes of an object when it is created. Automatically called every time a new instance 
# of a class is generated.

# self parameter is a convention in Python that refers to the instance of the class itself. Allows methods within
# a class to access and manipulate the instance's attributes and other methods.


print(Student.average(student))
# OR
print(student.average())
 """

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
student = Student("Bob", (100, 100, 95, 92, 91))
student2 = Student("Rolf", (91, 88, 78, 96, 95))
print(student.name)
print(student.average_grade())
print(student2.average_grade())