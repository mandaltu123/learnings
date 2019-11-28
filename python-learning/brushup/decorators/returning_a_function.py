def hello(name='Jose'):
    print("I am in hello function. Now based on passed in name we are going to return another function")

    def greet():
        return "\t This is the greet() function inside hello"

    def welcome():
        return "\t This is the welcome function inside hello"

    if name == 'Jose':
        return greet
    else:
        return welcome


if __name__ == '__main__':
    my_func = hello('Jose')
    print(my_func())
