# with importing collections.defaultdict()

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        mats = defaultdict(set)

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

                    if board[r][c] in mats[(r//3, c//3)]:
                        return False   
                    mats[(r//3, c//3)].add(board[r][c]) 
            
        return True
               




