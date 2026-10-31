from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        start = (-1, -1)
        queue: deque[tuple[int, int]] = deque([start])
        dist: dict[tuple[int, int], int] = {start: 0}

        while queue:
            i, j = queue.popleft()
            for dr, dc in (
                (-1, -1),
                (0, -1),
                (1, -1),
                (-1, 0),
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
            ):
                nr, nc = i + dr, j + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in dist
                    and grid[nr][nc] == 0
                ):
                    queue.append((nr, nc))
                    dist[(nr, nc)] = dist[(i, j)] + 1

        return dist.get((rows - 1, cols - 1), -1)

    def test(self):
        print(self.shortestPathBinaryMatrix([[0]]))
        print(self.shortestPathBinaryMatrix([[1]]))
        print(self.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
        print(self.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))


solution = Solution()

solution.test()
