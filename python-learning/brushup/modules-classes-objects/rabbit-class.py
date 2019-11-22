class Rabbit(object):

    def __init__(self, name):
        print("init method of bunny rabbit", name)
        self.name = name
        self.color = 'White'

    def move(self):
        print(f"{self.name} does not just walk, he always hops")


bunny = Rabbit("Mr Walker")
print(type(bunny))
print(f"{bunny.name} is a {type(bunny)} and his color is {bunny.color}")
bunny.move()