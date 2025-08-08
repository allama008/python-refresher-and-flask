def divide(dividend, divisor):
    if divisor == 0:
        # print("Divisor cannot be 0.")
        # return

        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor


# divide(15, 0)

# grades = [91, 92, 95, 88, 85]
# grades = []
# print("Welcome to the average grade program.")
""" 
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
 """

# In the above logic, you were trying the first statement and you were printing it inside the same try block. Print statement was
# put in the try block because the average variable is only created if the try block is successful, otherwise, it executes the 
# except block. Since average variable is not created then, therefore, that throws a separate error.
# NameError: name 'average' is not defined

# You don't need to try the print statement. You want to run the print statement if the try block is successful. To do that use the
# else block. The else block executes only if the try block is successful.
""" 
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    # print(e)
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you!")
 """
# As in C++, finally runs no matter what.

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Gen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")