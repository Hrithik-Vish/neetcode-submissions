# without importing collections.defaultdict()

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        mats = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] in row[r]:
                        return False
                    else:
                        row[r].add(board[r][c]) 

                    if board[r][c] in col[c]:
                        return False
                    else:
                        col[c].add(board[r][c]) 

                    if (r//3, c//3) not in mats:
                        mats[(r//3, c//3)] = set(board[r][c])

                    elif board[r][c] in mats[(r//3, c//3)]:
                        return False
                    else:
                        mats[(r//3, c//3)].add(board[r][c]) 
            
        return True
               




