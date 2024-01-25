class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        store = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    store[i][j] = store[i-1][j-1] + 1
                else:
                    store[i][j] = max(store[i-1][j], store[i][j-1])
        return store[n][m]