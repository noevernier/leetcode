import math
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = math.inf
        if n==1:
            return matrix[0][0]
        for i in range(n-2, -1, -1):
            for j, e in enumerate(matrix[i]):
                if j == 0:
                    matrix[i][j] = e + min(matrix[i+1][j], matrix[i+1][j+1])
                elif j==n-1:
                    matrix[i][j] = e + min(matrix[i+1][j], matrix[i+1][j-1])
                else:
                    matrix[i][j] = e + min(matrix[i+1][j], min(matrix[i+1][j-1],  matrix[i+1][j+1]))
                if i==0:
                    res = min(res, matrix[i][j])
        
        return res