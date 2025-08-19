users = [
    (0, "Bob", "password"),
    (1, "Rolf", "rolf123"),
    (2, "Jose", "jose456"),
    (3, "username", "longp4ssword"),
]

username_mapping = {user[1]: user for user in users}

print(username_mapping["Bob"])

""" 
#If the above mapping was not created, then we'd have to print in this way. Rather complicated
for user in users:
    if user[1] == "Bob":
        print(user)
 """

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Login granted")
else:
    print("Login credentials are incorrect")