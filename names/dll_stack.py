import sys
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # add item to the back of the stack
    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    # we execute from the back of the stack, deleting the last element after executing it
    def pop(self):
        if self.size < 1:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def __len__(self):
        return self.size

    # created and included mostly to find bugs
    def __str__(self):
        return f"{self.storage.__str__()}"