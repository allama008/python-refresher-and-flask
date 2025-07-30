"""
#An f-string allows us to embed variables inside of strings.


name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

name = "Rolf"

print(greeting)

greeting = f"Hello, {name}"
print(greeting)
"""

"""
# format string

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)

name = "Rolf"
print(with_name)
"""

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)