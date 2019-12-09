""""
This class will demonstrate different delete operations on a linked list
"""


class Node(object):
    """Initialize Node class"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Initialize linked list class"""

    def __init__(self):
        self.head = None

    # Function to add new node at the beginning
    def push(self, new_data):
        temp = self.head
        new_node = Node(new_data)
        if temp == Node:
            print(
                "since head is null that means this is an empty linked list. Making the new node as the first element")
            return new_node
        else:
            new_node.next = self.head
            self.head = new_node

    """
    Function to delete a node for a given key
    First let's formulate the steps via which we are going to delete a node for a given 
    1. Find the previous node to the node to be deleted
    2. change the next of the previous node
    3. free memory of the node to be deleted
    """

    def delete_node_for_a_given_key(self, key):
        temp = self.head
        # If the head node itself was requested to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp
                temp = None
                return

        # search for the node which has the key and keep track of the previous node as we will have to change the
        # previous.next
        while temp is not None:
            if temp.data == key:
                break
            previous = temp
            temp = temp.next
        # If key was not present in the linked list
        if temp is None:
            return
        previous.next = temp.next
        temp = None

    def delete_at_a_given_position(self, position):

        # if linked list is empty then just return, nothing to be done really
        if self.head is None:
            return

        # store the head in a temporary variable
        temp = self.head

        # if head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than the number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Node temp.next is the node to be deleted
        # Store the next pointer to next of the node to be deleted
        next_node = temp.next.next
        # de link the node from the linked list
        temp.next = None
        temp.next = next_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


# main execution starts here
if __name__ == '__main__':
    list = LinkedList()

    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    list.head = first
    first.next = second
    second.next = third
    third.next = fourth

    print("Node before deleting 3")
    list.print_list()
    print("\n")
    list.delete_node_for_a_given_key(3)
    print("Node after deleting 3")
    list.print_list()
    print("---------------------delete by position -----------------")
    list = LinkedList()

    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    list.head = first
    first.next = second
    second.next = third
    third.next = fourth

    print("Node before deleting 3")
    list.print_list()
    print("\n")
    list.delete_at_a_given_position(2)
    print("list after deleting at position 2")
    list.print_list()
