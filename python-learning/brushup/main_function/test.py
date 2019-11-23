# When we run a python file from command line python3 test.py, what python does is, it executes everything
# that is at the indentation level 0

from colorama import init
from colorama import Fore

init()


def myfunciton():
    print(Fore.YELLOW, "I am myfunciton")


if __name__ == "__main__":
    myfunciton()
print(Fore.BLUE + " hey there Delailah")
