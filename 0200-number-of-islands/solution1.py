from collections import deque


class Solution:
    def _bfs_grid(
        self,
        grid: list[list[str]],
        start: tuple[int, int],
        visited: set[tuple[int, int]],
    ):
        rows, cols = len(grid), len(grid[0])
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()

            i, j = node
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = i + dr, j + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == "1"
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    self._bfs_grid(grid, (row, col), visited)
                    island_count += 1

        return island_count

    def test(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        print(self.numIslands(grid))


solution = Solution()

solution.test()
