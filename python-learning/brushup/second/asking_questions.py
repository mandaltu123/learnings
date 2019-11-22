# Now we are going to try out how to take inputs from user and will play with them

# WARNING! We put an end=' ' at the end of each print line. This tells print to not end
# the line with a newline character and go to the next line.

print("How old are you ? ", end=' ')
age = input()
print("How tall are you ?", end=' ')
height = input()
print("How much do you weigh ?", end=' ')
weight = input()

print(f"So you are {age} old, {height} tall and {weight} heavy .")