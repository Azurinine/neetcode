class LRUCache:
    class Node():
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.n = self.p = None

    def __init__(self, capacity: int):
        self.h = self.Node(-1,-1)
        self.t = self.Node(-1,-1)

        self.h.p = self.t
        self.t.n = self.h

        self.cap = capacity
        self.keyToNode = {}

    def get(self, key: int) -> int:
        node = self.keyToNode.get(key)
        if not node:
            return -1

        # remove node from position
        node.n.p = node.p
        node.p.n = node.n

        # set node at front
        node.p = self.h.p
        node.n = self.h 

        node.p.n = node
        node.n.p = node
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.h.p.val = value
            return 
        
        # create new node
        node = self.Node(key, value)
        self.keyToNode[key] = node

        # insert at front
        node.n = self.h
        node.p = self.h.p

        self.h.p = node
        node.p.n = node

        if self.cap:
            self.cap -= 1
        else:
            rNode = self.t.n
            rNode.n.p = self.t
            self.t.n = rNode.n

            del self.keyToNode[rNode.key]






    


