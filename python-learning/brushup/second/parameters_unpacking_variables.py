# In this example we will see how to pass a variable to a python script and use them in the scipt

from sys import argv

# read the WYSS section for how to run this
# example how to run this : python parameters_unpacking_variables.py this is the

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)
