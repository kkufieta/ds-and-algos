
class LinkedListNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, list=None):
        self.head = None

        if list:
            self.create_from_array(list)

    def insert_node_before_head(self, node):
        if self.head:
            node.next = self.head

        self.head = node

    def create_from_array(self, arr):
        for val in arr[::-1]:
            self.insert_node_before_head(LinkedListNode(val))

    def as_array(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.data)
            node = node.next

        return arr