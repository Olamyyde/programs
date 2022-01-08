# def outer_fxn():
#     print("derat")

#     def inner_func():
#         print("tame")

#     # inner_fxn()
#     return inner_func

# inner_fxn = outer_fxn()
# inner_fxn()




# # Python decorator fxn
# import time

# def delay_decorator(func):
#     def wrapper_fxn():
#         time.sleep(2)
#         func()

#     return wrapper_fxn

# @delay_decorator
# def say_hello():
#     # time.sleep(2)
#     print("Hello")

# @delay_decorator
# def say_bye():
#     print("bye")

# def say_greeting():
#     print("How are you")

# say_bye()


# Advanced py decorator fxns

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated(func):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             func(args[0])
#     return wrapper

# @is_authenticated
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post")


# new_user = User("ollie")
# new_user.is_logged_in == True
# create_blog_post(new_user)




# Exercise
"""Create a logging_decorator() which is going to log the name of the function that was called,
 the arguments it was given and finally the returned output."""



def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You called {func.__name__}{args}")
        result = func(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


@logging_decorator
def multiply(a,b,c):
    return a*b*c

multiply(1,2,3)