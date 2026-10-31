from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        steps = -1

        start = []
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    start.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        queue = deque(start)
        while queue:
            steps += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

        if fresh > 0:
            return -1

        return max(steps, 0)
