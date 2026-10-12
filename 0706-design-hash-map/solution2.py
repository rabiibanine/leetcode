class MyHashMap:
    def __init__(self):
        self.size = 769
        self.count = 0
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        if not bucket:  # If the slot is empty before the append, increase the count
            self.count += 1

        bucket.append([key, value])

        if self.count / self.size > 0.7:
            self._resize()

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                if not bucket:  # If after the pop the slot is empty, decrease the count
                    self.count -= 1
                return

    def _hash(self, key: int) -> int:
        return key % self.size

    def _resize(self) -> None:
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        for bucket in old_buckets:
            for k, v in bucket:
                index = self._hash(k)
                new_bucket = self.buckets[index]
                new_bucket.append([k, v])
