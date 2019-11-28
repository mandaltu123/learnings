"""
In python we can have functions that can return another function.
In this example we are going to demonstrate that, this is actually a building block towards
decorators in python
"""


def hello():
    print("hello function is called now")
    return 'Hi Jose'


def other(some_func):
    """
    What we are doing here is that we are passing one function to this function, do some stuff and then
    will execute the function inside the print statement last line
    :param some_func: passed in function
    :return: does not return anything
    """
    print("Other function")
    print(some_func())


if __name__ == '__main__':
    other(hello)  # we are calling other function passing another function hello
