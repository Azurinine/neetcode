class PrefixTree:

    def __init__(self):
        self.charToNode = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            n = node.charToNode.get(c)
            if not n:
                n = PrefixTree()
                node.charToNode[c] = n   
            node = n
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            n = node.charToNode.get(c)
            if not n:
                return False
            node = n
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            n = node.charToNode.get(c)
            if not n:
                return False
            node = n
        
        return True
        
        