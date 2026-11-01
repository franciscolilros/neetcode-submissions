class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            temp = board[i].copy()
            
            for j in range(8, -1, -1):
                if temp[j] == ".":
                    temp.pop(j)
            
            if len(temp) > len(set(temp)):
                return False
        
            temp = []
            for j in range(9):
                temp.append(board[j][i])

            for j in range(8, -1, -1):
                if temp[j] == ".":
                    temp.pop(j)
            
            if len(temp) > len(set(temp)):
                return False

        

        for i in range(3):
            for j in range(3):
                temp = []
                for k in range(9):
                    d = k // 3
                    p = k % 3
                    temp.append(board[i*3 + p][j*3 + d])
                
                for j in range(8, -1, -1):
                    if temp[j] == ".":
                        temp.pop(j)
            
                if len(temp) > len(set(temp)):
                    return False
        return True
