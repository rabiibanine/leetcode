from collections import deque
from typing import final


@final
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if node is None:
            return None

        queue = deque([node])
        cloned = {node: Node(node.val)}

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                _ = cloned[current].neighbors.append(cloned[neighbor])

        return cloned[node]
