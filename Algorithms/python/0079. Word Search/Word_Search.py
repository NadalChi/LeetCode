class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i, j, index):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                if index == len(word) - 1 and word[index] == board[i][j]:
                    return True
                elif index == len(word) or word[index] != board[i][j]:
                    return False
                temp = board[i][j]
                board[i][j] = None
                res = search(i+1,j,index+1) or search(i,j+1,index+1) or search(i-1,j,index+1) or search(i,j-1,index+1)
                board[i][j] = temp
                return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, 0):
                    return True
                else:
                    pass
        return False
    