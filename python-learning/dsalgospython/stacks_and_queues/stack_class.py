""""A stack is a LIFO and linear data structure"""


class Stack(object):

    def __init__(self):
        # initialize an empty array
        self.items = []

    # Stack operations
    def is_empty(self):
        """returns True or False based whether stack is empty or not"""
        return self.items == []

    def push(self, data):
        """Push inserts an element at the end of the stack"""
        self.items.append(data)

    def pop(self):
        """pop always pops an item from the front of the stack"""
        return self.items.pop()

    def size_of_stack(self):
        return len(self.items)


# execution starts from here
if __name__ == '__main__':
    stack = Stack()
    # create a stack
    stack.push(1)
    stack.push(112)
    stack.push(33)
    stack.push(42)
    stack.push(15)
    print("size of stack after adding 5 items ", stack.size_of_stack())
    # now poo 1 item
    popped = stack.pop()
    print(f"popped item is {popped}")
    print(f"now the stack after popping one item {stack.size_of_stack()}")
