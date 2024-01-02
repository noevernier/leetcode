from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        if n==1:
            return 0 if nums[0]==target else -1

        if nums[left] <= nums[right]:
            idx = left
        else:
            while left < right - 1:
                mid = (left + right) // 2
                if nums[mid] > nums[left]:
                    left = mid
                else:
                    right = mid
            idx = left if nums[left] < nums[right] else right
        l = 0
        r = len(nums) - 1
        while l<=r:
            m = (r+l)//2
            m_r = (m+idx)%n
            if nums[m_r] == target:
                return m_r
            elif nums[m_r] > target:
                r = m - 1
            else:
                l = m + 1
        return -1