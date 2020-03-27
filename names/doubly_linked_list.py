"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        # increment length counter
        self.length += 1
        # if nothing's in the list, set new node to both head and tell
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # if list is non empty, 
        else:
            # set new_nodes next index to the old head, 
            new_node.next = self.head
            # set the old head's previous index (curently None) to the new head's index
            self.head.prev = new_node
            # set the head to the new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None:
            return self.head
        else:
            value = self.head.value
            self.delete(self.head)
            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            # set new_node.prev to be the old tail
            new_node.prev = self.tail
            # set the old tail.next to be the new tail
            self.tail.next = new_node
            # set the new_node to the new tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return "you are seeing this"
        else:
            value = self.tail.value
            self.delete(self.tail)
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # check if the node is already the head
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # check if the node is already the tail
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # check if the list has no elements in it 
        if self.length <= 0:
            return "Error: Cannot delete an element from an empty list."
        
        # adjust length of list
        self.length -= 1

        # check if the list has 1 element in it
        if self.head is self.tail:
            self.head = None
            self.tail = None

        # if more than one element
        # if the node to be deleted is the head:
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        # if the node to be deleted is the tail:
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        # if regular node
        else:
            node.delete()

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # check if empty
        if not self.head:
            return None
        
        max_value = self.head.value
        current_node = self.head
        # loop through the list
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        
        return max_value

    def __str__(self):
        elements = ""
        current_node = self.head

        while current_node:
            elements += f"{current_node.value}, "
            current_node = current_node.next
        return elements
        
