# 146


class LRUCache:
    class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.kv = {}

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1

        ret = self.kv[key]
        self.move_to_tail(key)
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            # Update key, value mapping and move to tail
            self.kv[key] = value
            self.move_to_tail(key)
            return

        if self.size == self.cap:
            # Cache is full, remove LRU cache first
            lru = self.head
            self.head = self.head.next  # Update head
            del self.kv[lru.val]  # Remove key val mapping
            self.size -= 1

        if self.size == 0:
            # If cache is empty, initialize self.head
            self.head = self.ListNode(key)
            self.tail = self.head  # Update tail
        else:
            # Cache has space, insert at tail
            self.tail.next = self.ListNode(key)
            self.tail = self.tail.next

        self.kv[key] = value  # Update key value mapping
        self.size += 1  # Update size

    def move_to_tail(self, key):
        """
        Helper function: move a node with value key to the tail
        """
        if self.tail.val == key:
            # Node is already at tail, terminate
            return

        if self.head.val == key:
            if not self.head.next:
                # Only node in cache, terminate
                return
            temp = self.head
            self.head = self.head.next
            self.tail.next = temp
            self.tail = temp
            return

        prev = None
        curr = self.head
        while curr and curr.val != key:
            # Find node
            prev = curr
            curr = curr.next

        # Move curr to tail
        prev.next = curr.next
        curr.next = None
        self.tail.next = curr
        self.tail = curr
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
