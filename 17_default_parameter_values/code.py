""" 
def add(x, y=8):
    print(x + y)

add(5, 8)
add(5)
 """
#default parameters must always go at the end.

default_y = 3

def add(x, y=default_y): #The value of default_y gets defined when the function gets created and it does not change later on even
    # if the variable is updated.
    sum = x + y
    print(sum)

add(2) #5

default_y = 4
add(2) #5