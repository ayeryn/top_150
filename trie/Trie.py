# 208


class Trie:
    # Tree approach - each node has at most 26 children i.e. a-z
    class Node:
        def __init__(self, val):
            self.val = val
            self.children = set()

    def __init__(self):
        self.root = self.Node("")

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            child = None
            for node in curr.children:
                if node.val == c:
                    child = node
                    break
            if not child:
                child = self.Node(c)
                curr.children.add(child)
            curr = child

    def search(self, word: str) -> bool:
        # BUG - prefix of any existing words also get added along the way
        curr = self.root
        for c in word:
            has = False
            for node in curr.children:
                if node.val == c:
                    has = True
                    curr = node
                    break

            if not has:
                return False

        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            has = False
            for node in curr.children:
                if node.val == c:
                    has = True
                    curr = node
                    break

            if not has:
                return False

        return True
