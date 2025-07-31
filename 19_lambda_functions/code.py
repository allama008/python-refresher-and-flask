""" 
def add(x, y):
    return x + y

print(add(5, 7))
 """
""" 
print((lambda x, y: x + y)(5, 7))

add = lambda x, y: x + y
print(add(5, 7))
 """

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [x * 2 for x in sequence]
doubled = [double(x) for x in sequence] #list comprehension is slightly faster.
doubled = list(map(double, sequence))

# Writing the same code with lambda functions
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))