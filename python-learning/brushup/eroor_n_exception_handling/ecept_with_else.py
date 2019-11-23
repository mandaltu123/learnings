def ask_for_int():
    while True:
        try:
            result = int(input("please provide an integer number > "))
        except ValueError:
            print("Oops! Looks like input is not a valid integer")
            continue
        else:
            print("Yes! thank you")
            break


if __name__ == "__main__":
    ask_for_int()
