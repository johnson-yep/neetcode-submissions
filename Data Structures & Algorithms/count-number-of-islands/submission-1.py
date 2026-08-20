class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, columns = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    visited.add((i, j))
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in directions:
                            nx, ny = x+dx, y+dy
                            
                            if (0 <= nx < rows and 0 <= ny < columns and (nx, ny) not in visited and grid[nx][ny] == "1"):    
                                visited.add((nx, ny))
                                stack.append((nx, ny))       

        return islands
                                           
        