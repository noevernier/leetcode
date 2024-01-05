from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum_product_left = [nums[0]]
        cum_product_right = [nums[-1]]
        n = len(nums)
        res = []
        for i in range(1, n):
            cum_product_left.append(nums[i]*cum_product_left[i-1])
            cum_product_right.append(nums[n-i-1]*cum_product_right[i-1])

        for i in range(n):
            if i > 0 and i < n-1:
                res.append(cum_product_left[i-1] * cum_product_right[n-(i+1)-1])
            elif i==0:
                res.append(cum_product_right[-2])
            else:
                res.append(cum_product_left[-2])
        return res