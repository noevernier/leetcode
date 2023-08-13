from ast import List
import numpy as np

class Solution:


    def checkLines(self, board_numpy):
        for i in range(len(board_numpy)):
            board_numpy_numbers = board_numpy[i][board_numpy[i] != "."]
            if(len(board_numpy_numbers) != len(set(board_numpy_numbers))):
                return False
        return True
    
    def checkBox(self, board_numpy):
        for i in range(0, len(board_numpy), 3):
            for j in range(0, len(board_numpy), 3):
                board_numpy_numbers = board_numpy[i:i+3, j:j+3].flatten()
                board_numpy_numbers = board_numpy_numbers[board_numpy_numbers != "."]
                if(len(board_numpy_numbers) != len(set(board_numpy_numbers))):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_numpy = np.array(board)
        return self.checkBox(board_numpy) and self.checkLines(board_numpy) and self.checkLines(np.transpose(board_numpy))