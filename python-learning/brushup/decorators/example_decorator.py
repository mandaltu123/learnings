def new_decorator(original_function):
    def wrap_function():
        print('Some extra code, before the original function')

        original_function()

        print('Some extra code after original function')

    return wrap_function


def hello():
    print("this is the original function")


if __name__ == '__main__':
    wrapped_function = new_decorator(hello)
    wrapped_function()
