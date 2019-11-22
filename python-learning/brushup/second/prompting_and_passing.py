# Let's do one excercise that uses argv and input() together to ask the user somethiing specific
# we will use this gyan in the next exercise where we will be doing file read and write

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script")
print("I would like to ask you a few questions")
print(f"Do you like me {user_name} ?")
likes = input(prompt)

print(f"where do you live {user_name} ?")
lives = input(prompt)

print("What kind of computer do you have ?")
computer = input(prompt)

print(f"""
Alright so putting it all together:
You live in {lives} and you said that you like me ? {likes}.
I am not sure though where that is.
And you have a {computer} computer, Nice.
""")
