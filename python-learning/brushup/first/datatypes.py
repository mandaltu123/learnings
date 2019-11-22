# python has following data types:


# int : integer numbers
# float : numbers with decimal points
# str : ordered sequence of characters
# list : ordered sequence of objects
# dict : unordered key value pairs
# tup : ordered immutable sequence of objects
# set : unordered collection of unique objects
# bool : logical value indicating true or false

# int
a = 10
print(type(a))

# boolean
b = 10.30
print(type(b))

# str
c = "this is my first string character sets" + ' ' + 'sammy'
print(type(c))
print(c)

# list
d = [10, "hello", 200.10, 'charset']
print(type(d))
print(d)

# dict
e = {"x": "100", "y": "200"}
print(type(e))
print(e)
print(e.get("x"))

# type
f = (
    10, "hello", 'there',
    30.50)  # tuple is ordered immutable sequence of objects. Once created, cannot change the object
# that is already in that sequence
print(type(f))
print(f)

# set
g = {"a", "a", "b", "c"}
print(type(g))
print(g)

# boolean
h = True
print(type(h))
print(h)
