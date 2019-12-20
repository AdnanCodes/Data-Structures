from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.cache = {} #Storing the keys in the dictionary for as it is easy and fast access to each item
        self.limit = limit #Default max size of the cache to 10 otherwise User defined when used
        self.size = 0 #Starting size of the cache
        self.storage = DoublyLinkedList() #Inititally tried to use Queue, I end up writing same functions of DLL
        #It will store key and its respective value as tuple
        #First position of tuple can used with 

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #Search for the key in the dictionary
        if key in self.cache:
            #when found, set it as a node for look up
            node = self.cache[key]

            #Delete the node from its existing position, and add to the Front
            #of the cache, in this DLL does this with method move to front
            self.storage.move_to_front(node)
            return node.value[1]
        else:#Don't return anything if item isn't found
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #Check for both caches, if key exist first then overwrite, otherwise make new entry and remove last item if exceeds the given limit
        #at end of each operation move them to front
        if key in self.cache: #Cache Hit when item is found otherwise Cache Miss
            #Overwrite the Node value and move it up front
            node = self.cache[key]
            node.value = (key,value) #Store node value as Tuple as node value itself won't modified but entire node is replaced.
            self.storage.move_to_front(node)
        else:
            #lets make new node and add it to the front of the cache and delete tail if it exeeds the size

            #If the size exceeds, remove tail node and its respective key in cache
            if self.size == self.limit:
                #Once max size reached, we will have to remove items that were least used aka least touch items,

                #Remove the key from cache and its linked pair which is this case is the tail
                #Retrieve key from tail node and then delete tail node 
                self.cache.pop(self.storage.tail.value[0])
                self.storage.remove_from_tail()
                #Now make space in size
                self.size -= 1
            
            #Now we can add element as normal

            self.storage.add_to_head((key,value))#Add the data point to front the list
            self.cache[key] = self.storage.head #Create new key in cache and link it up to newly created node
            self.size += 1#increase size of cache