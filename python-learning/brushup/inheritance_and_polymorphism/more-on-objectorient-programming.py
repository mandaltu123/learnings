class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # If you are coming for java background, this is the toString() method
    def __str__(self):
        return f"{self.title} by {self.author} which is of {self.pages} pages long"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has just been deleted")


b = Book('Python', 'Tuhin', 250)
print(b)  # without the __str__ method print(b) => <__main__.Book object at 0x7f50fd5f3290>
# but after implementing the __str__ method, it prints : Python by Tuhin which is of 250 pages long

length_of_book = len(b)
print(length_of_book)  # we will get TypeError: object of type 'Book' has no len()
# Now that we have implemented __len__ method that's why we are going to get output / length of the book
# as 250
del(b)
print(b)