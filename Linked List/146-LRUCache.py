# making a double linked list will help in easy insertion and removal. 
# keep two pointers to keep a track LRU node, first is LRU and last is RU.
# maps help in easy retrieval.
# time : O(1)

class Node():
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        
        self.cache = {}
        self.first, self.last = Node(0, 0), Node(0, 0)
        self.first.next, self.last.prev = self.last, self.first
        
    def insert(self, node):
        previous, nxt = self.last.prev, self.last
        previous.next = nxt.prev = node
        node.prev, node.next = previous, nxt
    
    def remove(self, node):
        previous, nxt = node.prev, node.next
        previous.next, nxt.prev = nxt, previous
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            node = self.first.next
            self.remove(node)
            del self.cache[node.key]