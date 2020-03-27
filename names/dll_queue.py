import sys
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # add item to the back of the queue
    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    # we execute from the front of the queue, deleting the first element after executing it
    def dequeue(self):
        if self.size < 1:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head() 

    def __len__(self):
        return self.size
