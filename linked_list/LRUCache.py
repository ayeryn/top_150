# 146


class LRUCache:
    # TODO: Optimize to get O(1)
    """
    Utilize a linked list structure such that:
    - The LRU cache node is always at head
    - The MRU cache node is always at tail
    - (aka. linked list is oldest to newest from front to back)
    - Updating an existing cache value bumps it to MRU
    """

    class ListNode:  # Nested ListNode class
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self, capacity: int):
        self.cap = capacity  # capacity
        self.size = 0  # current cache size
        self.head = None  # Init linked list
        self.tail = None
        self.kv = {}  # cache key, value mapping

    def get(self, key: int) -> int:
        if key not in self.kv:  # O(1)
            return -1

        ret = self.kv[key]  # O(1)
        self.move_to_tail(key)  # O(N)
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            # Update key, value mapping and move to tail
            self.kv[key] = value
            self.move_to_tail(key)  # O(N)
            return

        if self.size == self.cap:  # O(1)
            # Cache is full, remove LRU cache first
            lru = self.head
            self.head = self.head.next  # Update head
            del self.kv[lru.val]  # Remove key val mapping
            self.size -= 1

        if self.size == 0:  # O(1)
            # If cache is empty, initialize self.head
            self.head = self.ListNode(key)
            self.tail = self.head  # Update tail
        else:  # O(1)
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
            # Including when it's the only node in cache (head == tail)
            return

        if self.head.val == key:
            temp = self.head
            self.head = self.head.next
            self.tail.next = temp
            self.tail = temp
            return

        # Nodes between head and tail - O(N) worst case (tail.prev)
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
