""" 
def add(x, y):
    result = x + y
    print(result)
    #pass #means do nothing

add(5, 3)
 """
""" 
#Positional arguments
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello("Bob", "Smith")

 """

#Named arguments

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Bob", name="Smith")