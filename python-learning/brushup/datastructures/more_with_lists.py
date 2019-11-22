ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("wait there are not 10 things in that list. let's fix that")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print(f"adding {next_one}")
    stuff.append(next_one)

print("There we go:", stuff)
print("let's do something with the stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(len(stuff))
print(' '.join(stuff))  # oh! that's fancy
print(len(stuff))
print('#'.join(stuff[3:5]))
