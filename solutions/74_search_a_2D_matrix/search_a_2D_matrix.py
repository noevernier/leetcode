from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m, n = len(matrix), len(matrix[0])
        r = m * n - 1
        while l <= r:
            mid = (l+r) // 2
            i, j = mid//n, mid%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False