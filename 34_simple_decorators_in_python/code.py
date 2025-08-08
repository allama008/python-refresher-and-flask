user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

# Security risk
# print(get_admin_password())
""" 
# To secure it, we could use an if statement, but the function is still exposed and anyone could print it.
if(user["access_level"] == "admin"):
    print(get_admin_password())
 """
""" 
def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"
    
print(secure_get_admin())
 """
# All the places that you want secure access, you will be required to add the if statement. This can be done in another way
# using decorators in python.

# Decorators will allows us to modify our functions, to secure it, without having to replace all of our functions by its
# counterparts.
""" 
def secure_function(func):
    if(user["access_level"] == "admin"):
        return func
    
get_admin_password = secure_function(get_admin_password)

print(get_admin_password())
 """
# In the above code, since access_level is guest, therefore, it does not return func, it returns None. The next line then 
# tries to print None and this throws an error.
# OUTPUT
# TypeError: 'NoneType' object is not callable

# This error does not occur when the value in dictionary is changed from guest to admin.
# user = {"username": "jose", "access_level": "admin"}

# This is an issue because it is bad design to define and hard-code access_level. Instead you want to check for access_level
# values and decide accordingly.

def make_secure(func):
    def secure_function():
        if(user["access_level"] == "admin"):
            return func()
    return secure_function
    
get_admin_password = make_secure(get_admin_password)

print(get_admin_password())