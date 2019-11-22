# Now we have learnt how to read input from the user with input or argv.
# I have kept a dummy file here called test.txt. Run this python script as python file_reading.py test.txt
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the file name again")
file_again = input("> ")

text_again = open(file_again)
print(text_again.read())
