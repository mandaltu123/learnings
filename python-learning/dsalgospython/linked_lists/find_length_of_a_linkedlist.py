""""
This is a class with a method that shows how to find length of a linked list
"""


class Node(object):
    """Initialize the node class"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Initialize Linked list class"""

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def length_linked_list(self):
        length = 0
        temp = self.head
        if temp is None:
            return 0
        else:
            while temp is not None:
                length += 1
                temp = temp.next
        return length


if __name__ == '__main__':
    # create a linked list with 3 elements
    list = LinkedList()

    first = Node(1)
    second = Node(2)
    third = Node(3)

    list.head = first
    first.next = second
    second.next = third
    list.print_list()
    print(f"length of the list is = {list.length_linked_list()}")
