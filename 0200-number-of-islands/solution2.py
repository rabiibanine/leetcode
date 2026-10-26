class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self._check_neighbors(grid, (row, col))
                    count += 1

        return count

    def _check_neighbors(self, grid, node):
        row, col = node
        grid[row][col] = "2"

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[row]) and grid[nr][nc] == "1":
                self._check_neighbors(grid, (nr, nc))
