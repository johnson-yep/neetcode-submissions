class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maxArea = 0

        for row in range(rows):
            for col in range(columns):
                stack = []
                if grid[row][col] == 1:
                    stack.append((row, col))
                    area = 1
                    grid[row][col] = 0
                    while stack:
                        r, c = stack.pop()
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                                area += 1
                                stack.append((nr, nc))
                                grid[nr][nc] = 0

                    maxArea = max(maxArea, area)
        
        return maxArea
        
        