import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        out = self.storage.remove_from_head()
        if not out is None:
            self.size -= 1

        return out

    def len(self):
        return self.size
