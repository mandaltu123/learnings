# when you typed input() you were typing the (and) characters, which are parenthesis
# characters. This is similar to when you used to do a format with an extra variable,
# as iin f"{x} {y}". For input you can also put in a prompt to show to a person so that
# he knows what input he is going to give: it looks like this:
#
# y = input("Name ? ")
# This is how the user knows that he is asked to provide his name

age = input("How old are you ?")
height = input("How tall are you ?")
weight = input("how much do you weigh ?")

print(f"So you are {age} years old , and {height} inches tall and {weight} Kgs heavy")