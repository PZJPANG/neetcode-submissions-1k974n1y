class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            # Valid Each Row
            if not self.validRow(row):
                return False
            
            # Valid Each Column
            column = []
            for j in range(9):
                column.append(board[j][i])
            if not self.validRow(column):
                return False

        for i in range(0, 9, 3):
            # Valid Each Subbox
            for j in range(0, 7, 3):
                subbox = [board[i][j], board[i][j + 1], board[i][j + 2], board[i + 1][j], board[i + 1][j+ 1], board[i + 1][j+ 2], board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]]
                if not self.validRow(subbox):
                    return False
        
        return True
            
            
            
    
    def validRow(self, row):
        seen_num = {}
        for num in row:
            if num.isnumeric():
                if num in seen_num:
                    return False
                else:
                    seen_num[num] = True
        return True
    
