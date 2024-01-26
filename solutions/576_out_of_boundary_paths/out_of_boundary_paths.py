class Solution:
    def findPaths(self, m: int, n: int, N: int, x: int, y: int) -> int:
        max_v = 1000000000 + 7
        store = [[0] * n for _ in range(m)]
        store[x][y] = 1
        res = 0

        for _ in range(1, N + 1):
            buffer = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        res = (res + store[i][j]) % max_v
                    if j == 0:
                        res = (res + store[i][j]) % max_v
                    if i == m - 1:
                        res = (res + store[i][j]) % max_v
                    if j == n - 1:
                        res = (res + store[i][j]) % max_v
                    buffer[i][j] = (
                        (
                            (store[i - 1][j] if i > 0 else 0)
                            + (store[i + 1][j] if i < m - 1 else 0)
                        )
                        % max_v
                        + (
                            (store[i][j - 1] if j > 0 else 0)
                            + (store[i][j + 1] if j < n - 1 else 0)
                        )
                        % max_v
                    ) % max_v

            store = buffer

        return res
