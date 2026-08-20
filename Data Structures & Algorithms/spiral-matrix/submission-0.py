class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        spiral = []

        while l < r and t < b:
            for i in range(l, r):
                spiral.append(matrix[t][i])
            t += 1

            for i in range(t, b):
                spiral.append(matrix[i][r-1])
            r -= 1

            if not (l<r and t<b):
                break

            for i in range(r, l, -1):
                spiral.append(matrix[b-1][i-1])
            b -= 1

            for i in range(b, t, -1):
                spiral.append(matrix[i-1][l])
            l += 1
            

        return spiral
