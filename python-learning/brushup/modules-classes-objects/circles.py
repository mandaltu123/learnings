class Circle(object):
    # class attributes go here
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # Method to get circumference
    def get_circumference(self):
        return 2 * self.pi * self.radius

    # Method to get the are of the circle
    def get_area(self):
        return self.pi * pow(self.radius, 2)


circle = Circle(4)
circumference = circle.get_circumference()
area = circle.get_area()
print(f"circumference of our circle with radius 4 is {circumference} and the are is {area}")
