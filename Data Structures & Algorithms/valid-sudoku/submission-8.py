class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            check=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in check:
                    return False
                check.add(board[i][j])
        

        for i in range(9):
            check=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                if board[j][i] in check:
                    return False
                check.add(board[j][i])
        
        for boards in range(9):
            seen=set()
            
            board_row=(boards//3)*3
            board_col=(boards%3)*3

            for i in range(3):
                for j in range(3):
                    num_at_index=board[board_row+i][board_col+j]
                    if num_at_index==".":
                        continue
                    if num_at_index in seen:
                        return False
                    seen.add(num_at_index)
        return True



        