# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Doubly Linked List allows easily find the head or tail
        # It also helps with First In and First Out Approach
        # When enqueue we can use the tail pointer and when we dequeue we can use head pointer
        # Since DLL has methods constructed, we can use those to implement the Queue Class faster
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #To queue up, add the item to last of the linked list and increase its link by 1
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        #Make sure we are not dealing with empty Queue
        if self.size > 0:
            #Reduce the size and take out the item from the head (first out), returns the Value stored in that item
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
