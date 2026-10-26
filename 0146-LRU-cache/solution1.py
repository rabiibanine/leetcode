from typing import override


class Node:
    def __init__(
        self,
        key: int = 0,
        val: int = 0,
        prev: Node | None = None,
        next: Node | None = None,
    ):
        self.key: int = key
        self.val: int = val
        self.prev: Node | None = prev
        self.next: Node | None = next

    @override
    def __repr__(self):
        return f"Node({self.val})"


class DoublyLinkedList:
    def __init__(self, values: list[int] | None = None):
        self.head: Node = Node()
        self.tail: Node = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        if values:
            for value in values:
                node = Node(value)
                self.append(node)

    def prepend(self, node: Node):
        first = self.get_first()
        if first:
            self.head.next = node
            first.prev = node
            node.next = first
            node.prev = self.head
            return
        self.head.next = node
        self.tail.prev = node

    def append(self, node: Node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def move_to_end(self, node: Node):
        self.remove(node)
        self.append(node)

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def remove_first(self):
        first = self.get_first()
        if not first:
            return
        self.remove(first)

    def get_first(self) -> Node | None:
        first = self.head.next
        if first is self.tail:
            return None
        return first

    def get_last(self) -> Node | None:
        last = self.tail.prev
        if last is self.head:
            return None
        return last

    @override
    def __str__(self) -> str:
        values = []
        current = self.get_first()
        while current != None and current != self.tail:
            values.append(str(current.val))
            current = current.next

        return " -> ".join(values)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}
        self.dll: DoublyLinkedList = DoublyLinkedList()

    def get(self, key: int) -> int:
        if node := self.cache.get(key, None):
            self.dll.move_to_end(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.dll.move_to_end(node)
            return

        if len(self.cache) < self.capacity:
            node = Node(key, value)
            self.dll.append(node)
            self.cache[key] = node
            return

        first = self.dll.get_first()
        self.dll.remove_first()
        _ = self.cache.pop(first.key, None)

        node = Node(key, value)
        self.dll.append(node)
        self.cache[key] = node

    def test(self):
        self.put(1, 1)
        self.put(2, 2)
        self.get(1)
        print(self.dll)
        print(self.cache)
        self.dll.remove_first()
        print(self.dll)


lru_cache = LRUCache(2)

lru_cache.test()
