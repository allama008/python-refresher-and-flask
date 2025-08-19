""" 
a = []
b = a

# print(id(a))
# print(id(b))

a.append(35)

print(a)
print(b)

a = []
b = []

print(id(a))
print(id(b))
 """
# The fact that you can change a list after you've created it, means that the list is mutable.
# In python, all things are mutable, unless there are no ways of changing the properties of the object itself.
# Example - tuples
""" 
a = ()
b = ()
print(id(a))
a = a + (15,) # The id of a will change because this statement means you're creating a new tuple.

print(a)
print(id(a))
 """

a = 8597
b = 8597

print(id(a))
print(id(b))

# Python has this optimization when an integer is created, then it won't recreate it if another one identical to it is used.

b = b + 1

print(a)
print(b)

print(id(a))
print(id(b))

# Integers are immutable
# All things in python are mutable except for tuples, strings, integers, floats, and booleans.