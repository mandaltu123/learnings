class Animal(object):

    # init method
    def __init__(self):
        print("Animal is created")

    # Now we are going to add some behaviour to this animal
    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

    def speak(self):
        raise NotImplementedError("Hey this method needs to be implemented in the subclasses")


# Now let's do some inheritance stuff here
# we are going to create a dog class and say that dog inherits from animal
# because we all know that dog is also an animal

class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self)
        self.name = name
        print("Our dog is created")

    # Now we are going to override one of the methods from animal class
    def who_am_i(self):
        print("Hey I am a dog ..Woof!")

    # add new method
    def bark(self):
        print("Woof!")

    # Overriding the parent class method
    def speak(self):
        print(self.name, " says Woof!")


class Cat(Animal):

    def __init__(self, name):
        Animal.__init__(self)
        self.name = name

    def speak(self):
        print(self.name, " says meow!")


dog = Dog('Henderson')
type(dog)
dog.eat()  # calls the inherited method form animal class
dog.who_am_i()  # we have overridden this method, so now it will be called from the dog class
dog.bark()
dog.speak()

rodrigo = Cat("Rodrigo")
rodrigo.speak()

# Now try some fun stuffs here
for pet in [dog, rodrigo]:
    print(type(pet))
    print(pet.speak())


def speaking_tester(pet):
    print(type(pet))
    print(pet.speak())


speaking_tester(dog)
speaking_tester(rodrigo)
