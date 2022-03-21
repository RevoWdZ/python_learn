# function =    a block of code which is executed only when it is called.

# def hello(name):
#     print("Hello "+name)


# hello("Bro")

# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments


# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum


# print(add(1, 5, 6, 4))

# **kwargs =   parameter that will pack all arguments into a dictionary
#              useful so that a function can accept a varying amount of keyword arguments


def hello(**kwargs):
    #print("Hello " + kwargs['first']+" "+kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Bro", middle="Dude", last="Code")
