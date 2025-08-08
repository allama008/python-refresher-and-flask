import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."
        
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))

""" 
Took the code from the previous example. Let's say we want the get_password to include panel parameter in order to return different 
passwords based on different inputs. This would not work because the function has been wrapped by secure_function. Furthermore, if
the conditions of secure_function are met, then it return func() without any parameters, but get_password requires one parameter.

To resolve this, we add a parameter to each of the three functions - get_password, secure_function and func. This is not good because
we have coupled our make_secure decorator with the get_password function. We can't use the make_secure decorator with other functions
that take in different arguments.

To resolve this, we allow for unlimited arguments to cater for everything.
 """