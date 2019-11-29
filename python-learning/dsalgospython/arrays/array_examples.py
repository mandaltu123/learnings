cars = ["bwm", "audi", "mercedes"]

# check what is the type of this data structure
print(type(cars))  # this prints <class 'list'>. Meaning in python we create arrays with the help of
# data structure list
for car in cars:
    print(car)

# add some more items in the array
cars.append("renault")

print(cars)
# size of the cars array
print(len(cars))
print(cars.__sizeof__())  # Size of object in memory, in bytes.
# white a loop and get data from the index and print the element

i = 0
while i < len(cars):
    print(cars[i])
    i += 1
