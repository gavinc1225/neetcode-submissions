class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        conditions:
            - no duplicates in any row, col, or sub-box

        brute force
            1. 3 nested loops checking rows, cold, sub-box
            O(n^3)
        
        hash map
            - keep track of rows, cols, squares
            - at each cell verify if seen before
                - if yes then return false
            return true
        
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        val = 0

        for r in range(9):  
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        return True

                

        


        