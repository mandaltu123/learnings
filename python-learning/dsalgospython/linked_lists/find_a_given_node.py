"""Node class"""


class Node(object):

    def __init__(self, data):
        """Initializing a node"""
        self.data = data
        self.next = None


"""Linked list class"""


class LinkedList(object):

    def __init__(self):
        """Initializing a Linked list class"""
        self.head = None

    def find_an_element(self, x):
        current_node = self.head
        element_found = False
        while current_node is not None:
            if current_node.data == x:
                element_found = True
                break
            current_node = current_node.next
        return element_found


if __name__ == '__main__':
    list = LinkedList()
    global first, second, third
    first = Node(1)
    second = Node(2)
    third = Node(3)
    list.head = first
    first.next = second
    second.next = third
    found = list.find_an_element(2)
    print(f"is 2 in the list {found}")
    found = list.find_an_element(12)
    print(f"is 12 in the list {found}")
