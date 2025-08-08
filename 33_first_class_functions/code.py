# First class functions means that functions are just variables and you can pass them in as arguments to function and use
# them in the same way you would use any other variable.
""" 
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)
 """

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]
""" 
def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Bob Smith", get_friend_name))
 """

""" 
# Alternative - Use Lambda function
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
 """

# Another alternative - Use built-in function
from operator import itemgetter
print(search(friends, "Rolf Smith", itemgetter("name")))