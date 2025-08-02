def divide(dividend, divisor):
    return dividend / divisor

print("mymodule.py: ", __name__)
# OUTPUT
# mymodule.py:  __main__


# __name__ is a global variable in Python that changes depending on which file you're in. 
# It is a special variable because it will help you differentiate between the file you run and the file you import.

import libs.mylib