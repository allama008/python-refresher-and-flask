import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func) # This line tells secure_function that it is a wrapper for func (the function that is passed). This will keep the
    # name and documentation of the function get_admin_password intact and won't change it to secure_function
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."
        
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

# @make_secure is a shorthand of 
# get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
# OUTPUT (depending on the input dictionary "user")
# No admin permissions for jose.
# 1234

print(get_admin_password.__name__)
# OUTPUT
# secure_function
# The name of the function is changed internally. The function get_admin_password() is wrapped by the function secure_function.
# If you have any documentation attached to get_admin_password, then that will be lost because no documentation is attached to secure_function. Not sure what that means.
# To address this problem, we will use another decorator. 
# import functools
# @functools.wraps(func) 
