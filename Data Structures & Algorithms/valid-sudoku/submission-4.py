class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row=9
        col=9
        # Check For duplicate in rows.
        for i in range(row):
            li=set()
            for j in range(col):
                if board[i][j]==".":
                    continue
                if board[i][j] in li:
                        return False
                li.add(board[i][j])
                
        # Check for duplicate in columns.
        for i in range(row):
            li=set()
            for j in range(col):
                if board[j][i]==".":
                    continue
                
                if board[j][i] in li:
                        return False
                li.add(board[j][i])

        for box in range(9):
            seen=set()
            box_row=(box//3)*3
            box_col=(box%3)*3

            for i in range(3):
                for j in range(3):
                    num_in_box=board[box_row+i][box_col+j]
                    if num_in_box==".":
                        continue
                    if num_in_box in seen:
                        return False
                    seen.add(num_in_box)
        return True





        


        

        







        