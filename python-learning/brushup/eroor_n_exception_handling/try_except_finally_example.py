def add(a, b):
    try:
        print(a + b)
    except TypeError:
        print("something happened")
    else:
        print("in else")
    finally:
        print("in finally")


add(10, 20)

number1 = 10
number2 = input("Please provide a number > ")
add(number1, number2)
