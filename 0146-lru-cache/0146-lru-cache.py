class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d[key] = self.d.pop(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
        elif len(self.d) >= self.cap:
            self.d.pop(next(iter(self.d)))
        self.d[key] = value
