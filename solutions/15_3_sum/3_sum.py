from typing import List

class Solution:
    def counting_sort(self, nums):
        max_num = max(nums)
        count = [0] * (max_num + 1)
        for num in nums:
            count[num] += 1
        sorted_nums = []
        for i in range(len(count)):
            sorted_nums.extend([i] * count[i])
        return sorted_nums

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        min_v = min(nums)
        nums = self.counting_sort(nums+min_v)
        n = len(nums)
        triplets = []
        for i in range(nums):
            if(i > 0):
                while(nums[i] == nums[i-1]):
                    continue
            target = 3*min_v - nums[i]
            l, r = i+1, n-1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return triplets
            
            