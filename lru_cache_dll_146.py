
class Node():
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

# Doubly LL
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return None

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        return None


# OrderedDict implementation
class LRUCache:

    def __init__(self, capacity: int):
        import collections
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
        self.dic.move_to_end(key)
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# ------------------- TEST CASES -------------------
def test_lru_cache():
    print("Test 1: Basic put/get")
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1, "Test 1 failed: get(1) should return 1"

    print("Test 2: Capacity eviction")
    lru.put(3, 3)  # evicts key 2
    assert lru.get(2) is None, "Test 2 failed: get(2) should return None (evicted)"

    print("Test 3: Update existing key")
    lru.put(1, 10)
    assert lru.get(1) == 10, "Test 3 failed: get(1) should return updated value 10"

    print("Test 4: LRU order maintenance")
    lru.put(4, 4)  # evicts key 3
    assert lru.get(3) is None, "Test 4 failed: get(3) should return None (evicted)"
    assert lru.get(4) == 4, "Test 4 failed: get(4) should return 4"

    print("Test 5: Access order changes LRU")
    lru.get(1)  # now 4 is LRU
    lru.put(5, 5)  # evicts key 4
    assert lru.get(4) is None, "Test 5 failed: get(4) should return None (evicted)"
    assert lru.get(1) == 10, "Test 5 failed: get(1) should return 10"
    assert lru.get(5) == 5, "Test 5 failed: get(5) should return 5"
    print("All tests passed!")

if __name__ == "__main__":
    test_lru_cache()