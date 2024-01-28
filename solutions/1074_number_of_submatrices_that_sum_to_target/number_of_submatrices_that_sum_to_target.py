from collections import defaultdict
from typing import List

class Solution:
    def getCount(self, prefix, target):
        m = defaultdict(int)
        s = 0
        ans = 0
        m[0] = 1
        for i in prefix:
            s += i
            if s - target in m:
                ans += m[s - target]
            m[s] += 1
        return ans

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for i in range(m):
            prefix = [0] * n
            for j in range(i, m):
                for k in range(n):
                    prefix[k] += matrix[j][k]
                ans += self.getCount(prefix, target)

        return ans