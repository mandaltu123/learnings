print("lets practice everything")
print('you\'d need to know \'bout escapes withh \\ that do:')
print('\n newlines and \t tabs')

poem = """
Hey! Mr. Tambourine man, play a song for me
I'm not sleepy and there is no place I'm going to
Hey! Mr. Tambourine man, play a song for me
In the jingle jangle morning I'll come following you
Though I know that evening's empire has returned into sand
Vanished from my hand
Left me blindly here to stand but still not sleeping
My weariness amazes me, I'm branded on my feet
I have no one to meet
And the ancient empty street's too dead for dreaming
"""

print("---------------------")
print(poem)
print("---------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000
beans, jars, crates = secret_formula(start_point)

# Remember this is another way of formatting string
print("with a starting_point of: {}".format(start_point))
# It's just like f"" string
print(f"we'd have {beans} beans, {jars} jars and {crates} crates")

start_point = 10
print("we could also do this way:")
formula = secret_formula(start_point)
# This is a easy way to apply a list to a format string
print("we'd have {} beans, {} jars and {} crates.".format(*formula))
