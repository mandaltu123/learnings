class Animal(object):
    # This is the place where we are going to put the class level attributes
    # Class level attributes are those which are typically not going to change over time
    species = 'mammal'

    # init method for the initialization, since I am coming from java background, this is the constructor of this class
    def __init__(self, animal_type, name):
        self.animal_type = animal_type
        self.name = name

    # Now let's add some behavior or action to this Animal class
    def make_sound(self):
        if self.animal_type == 'dog':
            print(f'Whoof says {self.name}')
        elif self.animal_type == 'cat':
            print(f"Meaw says {self.name}")
        else:
            print("I don't know what to do")


dog = Animal('dog', 'Scooby')
dog.make_sound()
cat = Animal('cat', 'Fluffy')
cat.make_sound()
