""" def hello():
    print("Hello!")

hello() """

""" 
def user_age_in_seconds():
    user_age = int(input("Enter you age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

user_age_in_seconds()
 """
""" 
friends = ["Rolf", "Bob"]

def add_friends():
    friend_name = input("Enter your friend's name: ")
    #friends = friends + [friend_name] #This won't add the new name to the global list. Python creates a local scope for the variable.
    # Two variables friends - one with local scope and the other with global.
    f = friends + [friend_name]
add_friends()
 """

