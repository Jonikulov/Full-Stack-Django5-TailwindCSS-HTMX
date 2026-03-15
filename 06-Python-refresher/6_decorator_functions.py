import functools

# Decorator Functions

user = {"username": "john", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)  # Standard practice: preserves introspection (name, docstrings, ...) of the wrapped function
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user["username"]!r}."

    return secure_function


@make_secure
def get_admin_pass(panel):
    if panel == "billing":
        return "12345"
    elif panel == "dashboard":
        return "super_secret_password"


print(get_admin_pass("billing"))
print(get_admin_pass.__name__, end="\n\n")

###############################################################################
# Decorators with Parameters

user = {"username": "john", "access_level": "admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No admin permissions for {user["username"]!r}."

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_pass(panel):
    if panel == "billing":
        return "12345"
    elif panel == "dashboard":
        return "super_secret_password"

print(get_admin_pass("dashboard"))
