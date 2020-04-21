import collections

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            v = self.cache.pop(key)
            self.cache[key] = v
            return v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             # touch
#             for k in self.cache:
#                 self.cache[k][1] -= 1
#             self.cache[key][1] = self.capacity
#             print(self.cache[key][0])
#             return self.cache[key][0]

#         else:
#             print(-1)
#             return -1

#     def put(self, key: int, value: int) -> None:
#         for k in self.cache:
#             self.cache[k][1] -= 1
#         if len(self.cache) < self.capacity or key in self.cache:
#             self.cache[key] = [value, self.capacity]

#         else:
#             min_k = min(self.cache, key=lambda k: self.cache[k][1])
#             del self.cache[min_k]

#             self.cache[key] = [value, self.capacity]
#         print(self.cache)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
