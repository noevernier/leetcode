from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)//3
        for i in range(n):
            if nums[3*i+2]-nums[3*i]> k: return []
            res.append(nums[3*i:3*i+3])
        return res