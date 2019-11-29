"""A simple class to implement linked list """


class Node(object):
    """This is the node class. Node class contains properties data and next pointer """

    # function that initializes the Node object
    def __init__(self, data):
        """constructor which takes data as an input and sets next pointer to None by default"""
        self.data = data
        self.next = None


""" This is the linked list class, will have have different operation implementations in it"""


class LinkedList(object):

    # Function to initialize head
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# code execution starts here
if __name__ == "__main__":
    # create an empty list
    llist = LinkedList()

    llist.head = Node(1)
    secondNode = Node(2)
    thirdNode = Node(3)

    llist.head.next = secondNode
    secondNode.next = thirdNode
    llist.print_list()
