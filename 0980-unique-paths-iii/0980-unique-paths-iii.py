class Solution:
    def uniquePathsIII(self, grid):
        self.rows = len(grid)
        self.cols = len(grid[0])
        empty = 0
        startRow = 0
        startCol = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 0:
                    empty += 1
                if grid[r][c] == 1:
                    startRow = r
                    startCol = c

        return self.dfs(grid, startRow, startCol, empty)

    def dfs(self, grid, r, c, empty):
        # Boundary / obstacle
        if (r < 0 or r >= self.rows or
            c < 0 or c >= self.cols or
            grid[r][c] == -1):
            return 0

        # Destination
        if grid[r][c] == 2:
            return 1 if empty == 0 else 0

        temp = grid[r][c]

        # Visit an empty cell
        if grid[r][c] == 0:
            empty -= 1

        # Mark as visited
        grid[r][c] = -1

        paths = (
            self.dfs(grid, r + 1, c, empty) +  # down
            self.dfs(grid, r - 1, c, empty) +  # up
            self.dfs(grid, r, c + 1, empty) +  # right
            self.dfs(grid, r, c - 1, empty)    # left
        )

        # Backtracking
        grid[r][c] = temp

        return paths