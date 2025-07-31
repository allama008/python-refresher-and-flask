""" 
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total
# function has a set of arguments that will be collected into a tuple of arguments.

print(multiply(1, 3, 5))
 """
""" 
# Just like we use the asterisk to collect values into one parameter, we can also use asterisk to destructure a variable into multiple arguments.
def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums)) 
 """

""" 
def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))
# OR
print(add(**nums)) # You've a dictionary with two keys, therefore, I'm going to pass in each key as a named argument
# and the value will be that associated with the key.
 """

def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total
 
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

#Collect all the positional arguments into args and also have a named argument at the end.
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."
    
print(apply(1, 3, 6, 7, operator="*"))
""" 
def apply(*args, operator) collects all the arguments as a tuple. This tuple is then passed through the 
return multiply(args) statement. The multiply(*args) function collects it as a tuple, thereby making it
a tuple of tuple. The arg variable in the for loop extracts a tuple from the tuple of tuple and multiplies
it with 1 and returns that tuple.
To resolve this issue, we can simply change it to return multiply(*args) so as to destructure the variable.
 """