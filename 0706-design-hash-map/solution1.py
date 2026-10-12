class MyHashMap:
    def __init__(self):
        self.array: list[int] = [-1] * 1000000
        self.items_num: int = 0

    def put(self, key: int, value: int) -> None:

        index = self._hash(key)

        if index < len(self.array) and self.array[index] == -1:
            self.items_num += 1

        self.array[index] = value

        if self._get_load_factor() > 0.7:
            self.array += [-1] * 10

    def get(self, key: int) -> int:
        index = self._hash(key)
        if len(self.array) <= key:
            return -1
        return self.array[index]

    def remove(self, key: int) -> None:
        index = self._hash(key)

        if index < len(self.array) and self.array[index] != -1:
            self.items_num -= 1
            self.array[index] = -1

    def _hash(self, key: int) -> int:
        return key

    def _get_load_factor(self) -> float:
        return self.items_num / len(self.array)

    def test(self):
        array = []
        array[4] = 5
        print(array)


my_hash_map = MyHashMap()

my_hash_map.test()
