class Dog(object):

    def __init__(self, breed):
        self.breed = breed


milo = Dog('Lab')
print(type(milo))
print(milo.breed)

