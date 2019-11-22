# Yes now its the time to introduce functions. Functions basically do these three things
# 1.      They name pieces of code the way variables name strings and numbers
# 2.      They take arguments the way scripts take argv
# 3.      Using point number 1 and 2 they let us write our own mini scripts or timy commands
# This one is like your scripts with argv


# 1.
# We tell Python we want to make a function using def for “define.
#
# On the same line as def we give the function a name. In this case we just called it “print_two,”
# but it could also be “peanuts.” It doesn’t matter, except that your function should have a short
# name that says what it does.
# 3.
# We tell it we want *args (asterisk args), which is a lot like your argv parameter but for func-tions.
# This has to go inside parentheses to work.
# 4. We end this line with a : (colon) and start indenting.
# 5. After the colon, all the lines that are indented four spaces will become attached to print_two.
# Our first indented line is one that unpacks the arguments, the same as with your scripts.
# 6.
# To demonstrate how it works we print these arguments out, just like we would in a script.


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} and arg2: {arg2}")


# that * args is just pointless, we can do something like this
def print_tow_again(arg1, arg2):
    print(f"arg1: {arg1} and arg2: {arg2}")


# This just takes one argument
def print_one(arg1):
    print(f"the argument is {arg1}")


# This one takes no arguments
def print_no_argument():
    print("Ola amigo.")


# Now let's call all these functions one by one
print_two("courtney", "cox")
print_tow_again("courtney", "cox")
print_one("courtney")
print_no_argument()
