# 208


class Trie:
    # BST approach
    def __init__(self):
        self.tree = []

    def insert(self, word: str) -> None:
        if len(self.tree) == 0:
            self.tree.append(word)
        else:
            # binary insert
            left, right = 0, len(self.tree)
            while left < right:
                mid = (left + right) // 2
                if self.tree[mid] == word:
                    return

                if self.tree[mid] < word:
                    left = mid + 1
                else:
                    right = mid

            # left is insertion point
            self.tree = self.tree[:left] + [word] + self.tree[left:]

    def search(self, word: str) -> bool:
        if len(self.tree) == 0:
            return False
        left, right = 0, len(self.tree) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.tree[mid] == word:
                return True

            if self.tree[mid] < word:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def startsWith(self, prefix: str) -> bool:
        if len(self.tree) == 0:
            return False

        l = len(prefix)
        left, right = 0, len(self.tree) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.tree[mid][:l] == prefix:
                return True

            if self.tree[mid] < prefix:
                left = mid + 1
            else:
                right = mid - 1

        return False
