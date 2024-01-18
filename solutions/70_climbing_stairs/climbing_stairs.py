class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        step_n_1 = 1
        step_n = 2
        i=0
        while i < n-2:
            step_n, step_n_1 = step_n + step_n_1, step_n
            i+=1
        return step_n
