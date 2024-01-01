from typing import List

class Solution:
    def f(self, k, piles):
        t = 0
        for p in piles:
            t += (p // k) + (p%k != 0)
        return t
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles) + 1
        k_min = 1
        res = k_max
        while k_max >= k_min:
            mid = (k_max + k_min) // 2
            if self.f(mid, piles) <= h:
                k_max = mid - 1
                res = mid
            else:
                k_min = mid + 1
        return res
        