class PrefixTree:

    def __init__(self):
        self.charToNode = {}

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            n = node.charToNode.get(c)
            if not n:
                n = PrefixTree()
                node.charToNode[c] = n   
            node = n
        node.charToNode['*'] = PrefixTree()

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            n = node.charToNode.get(c)
            if not n:
                return False
            node = n
        return '*' in node.charToNode

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            n = node.charToNode.get(c)
            if not n:
                return False
            node = n
        
        return True
        
        