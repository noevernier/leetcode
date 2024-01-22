from collections import Counter
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        diff = n * (n+1)//2 - sum(nums)

        for i in range(n):
            if c[nums[i]] > 1:
                return [nums[i], nums[i]+diff]