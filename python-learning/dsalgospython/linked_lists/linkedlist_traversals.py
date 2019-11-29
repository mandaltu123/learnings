"""Class where we are going to create a Linked List with 3 nodes and then will see how to traverse and print elements"""


class Node(object):

    # initialize a Node object
    def __init__(self, data):
        self.data = data
        self.next = None  # next pointer should be None while initializing a linked list node


class LinkedList(object):

    # Initialize Linked List object

    def __init__(self):
        """Initialize a linked list object abd set the Head to null as initially there will be only
        one node in the linked list"""
        self.head = None

    # define a method to iterate over the list and print each element
    def print_list(self):
        tmp = self.head
        while (tmp):
            print(tmp.data)
            tmp = tmp.next


# code execution starts from here

if __name__ == "__main__":
    llist = LinkedList()

    first = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head = first
    first.next = second
    second.next = third

    llist.print_list()
