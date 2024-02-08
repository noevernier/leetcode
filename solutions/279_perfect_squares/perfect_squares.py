class Solution:
    def numSquares(self, n: int) -> int:
        perfect_square = []
        i = 1
        while i*i <= n:
            perfect_square.append(i*i)
            i += 1
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in perfect_square:
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]