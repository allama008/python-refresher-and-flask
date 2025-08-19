#x = (5, 11) #x = 5 

#x, y = 5, 11
"""
t = 5, 11
x, y = t
print(x, y) 
"""

""" student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)
    # print(f"{student}: {attendance}") """

""" for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}") """    

# people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

""" for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}") """

# Above method fails when a value is missing, for example
# people = [("Bob", 42), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
# ValueError: not enough values to unpack (expected 3, got 2)

# for person in people:
#     print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")
""" 
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession) """

""" head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail) """
# 1
# [2, 3, 4, 5]

""" *head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail) """
# [1, 2, 3, 4]
# 5