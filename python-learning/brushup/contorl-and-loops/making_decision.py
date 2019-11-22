print("""
You enter a dark room with two doors.
Do you go through door #1 or door #2?
""")

door = input("> ")
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    if bear == "1":
        print("the bear eats your legs off. great job")
    elif bear == "2":
        print("bear eats of face off, fantastic job")
    else:
        print("bear runs away")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("good job")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("you stumble around and fall on a knife and die. Good Job!")
