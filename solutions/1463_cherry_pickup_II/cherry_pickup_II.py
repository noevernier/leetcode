from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]
        
        for j in range(cols):
            for k in range(j+1, cols):
                dp[-1][j][k] = grid[rows-1][j] + grid[rows-1][k]
                
        for i in range(rows-2, -1, -1):
            for j in range(cols):
                for k in range(j+1, cols):
                    max_cherries = 0
                    for pj in [j-1, j, j+1]:
                        for pk in [k-1, k, k+1]:
                            if 0 <= pj < cols and 0 <= pk < cols:
                                max_cherries = max(max_cherries, dp[i+1][pj][pk])
                    dp[i][j][k] = max_cherries + grid[i][j] + (grid[i][k] if j != k else 0)
        
        return dp[0][0][cols-1]