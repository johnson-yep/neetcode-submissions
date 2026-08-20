class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, columns = len(matrix), len(matrix[0])
        zeros = []
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    zeros.append((r, c))

        for r, c in zeros:
            for i in range(columns):
                matrix[r][i] = 0
            for i in range(rows):
                matrix[i][c] = 0