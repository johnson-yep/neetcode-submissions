class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # check rows
        for i in board:
            seen = set()
            for j in i:
                if j in seen:
                    return False
                if  j != ".":
                    seen.add(j)
        
        # check columns
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[j][i] in seen:
                    return False

                if board[j][i] != ".":
                    seen.add(board[j][i])

        # check squares
        seen = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(n):
            for j in range(n):
                x, y = int(i/3), int(j/3)

                if board[i][j] in seen[x][y]:
                    return False
                
                if board[i][j] != ".":
                    seen[x][y].add(board[i][j])

        return True

