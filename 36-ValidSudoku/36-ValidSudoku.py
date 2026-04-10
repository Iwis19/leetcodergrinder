class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        """
        already did this in bruteforce on neetcode, so this is a hashset solution

        1. learned that python does operations left to right (obv shouldve known this), so i messed up on 
        square_id = 3*(row_id//3) + col_id//3, because without the brackets, it basically meant 
        square_id = row_id + col_id//3
        2. wasnt very much keeping in mind that row_id was just an integer, not the actual sub array in the 2d array
        board itself
        3. learned that sets have way faster lookup than arrays O(n) vs O(1) 

        0 ms runtime beats 100
        """

        rows = [ set() for _ in range(9) ]
        cols = [ set() for _ in range(9) ]
        squares = [ set() for _ in range(9) ]

        for row_id in range(len(board)):
            for col_id in range(len(board[row_id])):

                curr = board[row_id][col_id]
                if curr == ".":
                    continue
                square_id = 3*(row_id//3) + col_id//3

                if (curr in rows[row_id]) or (curr in cols[col_id]) or (curr in squares[square_id]):
                    return False

                rows[row_id].add(curr)
                cols[col_id].add(curr)
                squares[square_id].add(curr)

        return True





