class Cat(object):

    def __init__(self, no_of_legs):
        print("this is my cat")
        self.no_of_legs = no_of_legs
        print(f"Passed in number of legs is {no_of_legs}")


cat = Cat(4)
print(type(cat))
print(cat.no_of_legs)
