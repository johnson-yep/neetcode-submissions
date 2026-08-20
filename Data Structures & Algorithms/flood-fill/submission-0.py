class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
            
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, columns = len(image), len(image[0])

        newImage = image.copy()
        stack = [(sr, sc)]
        curColor = newImage[sr][sc]
        newImage[sr][sc] = color
        
        while stack:
            r, c = stack.pop()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if (0 <= nr < rows) and (0 <= nc < columns) and (newImage[nr][nc] == curColor):
                    newImage[nr][nc] = color
                    stack.append((nr, nc))

        return newImage