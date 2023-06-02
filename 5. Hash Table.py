class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for kv in self.arr[hash]:
            if kv[0] == key:
                return kv[1]
        return None

    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        if self.arr[hash]:
            for idx, element in enumerate(self.arr[hash]):
                if idx == key:
                    self.arr[hash].remove((idx, element))
                    break
        self.arr[hash].append((key, val))

    def __delitem__(self, key):
        hash = self.get_hash(key)
        if self.arr[hash]:
            for idx, element in enumerate(self.arr[hash]):
                if idx == key:
                    self.arr[hash].remove((idx, element))
                    break
