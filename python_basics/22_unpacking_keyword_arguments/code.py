""" 
def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)
# OUTPUT
# {'name': 'Bob', 'age': 25}
 """
""" 
def named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named(**details)
# OUTPUT
# Bob 25
# The above treats the key as the named argument.
 """
""" 
def named(**kwargs):
    print(kwargs)

details = {"name": "Bob", "age": 25}

named(**details)
# OUTPUT
# {'name': 'Bob', 'age': 25}
 """

""" 
def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)
 """

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 4, name="Bob", age=25)