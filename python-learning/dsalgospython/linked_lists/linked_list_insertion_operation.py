"""In this class we will implement methods to insert a new node in linked list. A node can be added in three ways

1) At the front of the linked list
2) After a given node.
3) At the end of the linked list."""


# first create the node class
class Node(object):
    """initialize the node class"""

    def __init__(self, data):
        self.data = data
        self.next = None  # a new node will not have a next pointer

    """Here we are going to have the actual linked list implementation """


class LinkedList(object):
    """Initialize Linked list class"""

    def __init__(self):
        self.head = None  # New linked list's head will point to None at creation

    def insert_at_the_beginning(self, data):
        """This method creates a new node and inserts it at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """This method inserts a new node at the end of the linked list"""
        # create a new node
        new_node = Node(data)

        # iterate over the current list
        # find the last node
        # then add the item at the end
        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        # changing the last pointer's next node to point to the newly inserted node
        last_node.next = new_node

    def insert_after_item(self, x, data):
        """This method inserts an element after given element"""
        current_node = self.head
        while current_node is not None:
            if current_node.data == x:
                break
            current_node = current_node.next
        if current_node is None:
            print("Item not in the list...")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


def test_isert_at_start_or_end():
    global first, second, third, llist1
    llist = LinkedList()
    # create a linked list with 3 nodes
    first = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head = first
    first.next = second
    second.next = third
    print("the initial list")
    llist.print_list()
    # add 5 as new node at the beginning of the list
    llist.insert_at_the_beginning(5)
    print("new list after adding 5 at the beginning ")
    llist.print_list()
    # add a new node at the end which is 10
    llist.insert_at_end(10)
    print("linked list after adding node 10 at the end")
    llist.print_list()
    # test inserting node after given item
    llist1 = LinkedList()


def test_insert_after_given_item():
    global first, second, third
    first = Node(1)
    second = Node(2)
    third = Node(3)
    llist1.head = first
    first.next = second
    second.next = third
    print("list before insertion \n")
    llist1.print_list()
    llist1.insert_after_item(2, 99)
    print("list after insertion ")
    llist1.print_list()


# main execution will start from here
if __name__ == "__main__":
    test_isert_at_start_or_end()
    # create a linked list with 3 nodes
    test_insert_after_given_item()
