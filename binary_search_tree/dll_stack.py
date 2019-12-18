# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Stack is similar to queue except we will deal with tail node exclusively, it will easier to add or remove the last item of doubly linked list, and repoint accordingly
        self.storage = DoublyLinkedList()

    def push(self, value):
        #Stacks always add from top, add item  to the tail and increase it size
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        #Stacks removes from top so it will always be the tail, remove item and reduce size
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
