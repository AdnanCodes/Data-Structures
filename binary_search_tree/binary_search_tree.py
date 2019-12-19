import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

            #Root occupied when class is instantiated, check whether it is smaller or bigger, respectively goes to left or right
        if(value < self.value):
            if self.left == None: #if there is no leaf, spawn new tree node
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)#otherwise attempt insert from left node as starting node 
        elif(value >= self.value):
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Start by comparing the target value
        if target < self.value:#If less, check if node is empty, then reached base case and target doesn't exist in the tree
            if self.left is None:
                return False
            return self.left.contains(target)#Otherwise recursion from left node and try finding it
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:#if target value isn't less or greater, then it found the node
            return True


    # Return the maximum value found in the tree
    def get_max(self): #Go right for maximum value
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):#Run the function the, start recursion on left and right, it will be stop once functions runs on all nodes
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            #start left, print to the root, then print the right ones
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #Using Queue DS
        queue = Queue()

        #Enqueue the node and loop through
        queue.enqueue(node)

        while queue.size>0:
            #Remove from queue and Make it current node to print and iterate through
            current = queue.dequeue()
            if current:
                print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #Using Stack DS
        stack = Stack()

        #Push the node and Loop through
        stack.push(node)

        while stack.size> 0:
            #Remove the stack to make it current node and print and iterate through
            current = stack.pop()

            if current:
                print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            #print to the root,then left node then print the right ones
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
