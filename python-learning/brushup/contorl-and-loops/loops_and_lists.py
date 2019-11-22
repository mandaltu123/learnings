the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'mango', 'banana', 'apricot']
change = [1, "car", 3.50, 'quarters']

# The first kind of for-loop is something that goes through the list
for number in the_count:
    print(f"This number is {number}")

# second for loop that iterate over the fruit list
for fruit in fruits:
    print(f"Fruit is {fruit}")

# Also we can go through mixed list too
# notice we have to use {} since we don't know the type in advance
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function
for i in range(0, 6):
    print(f"adding {i} into the list")
    elements.append(i)

# Now we can print those elements too
for i in elements:
    print(f"The element I got out is {i}")
