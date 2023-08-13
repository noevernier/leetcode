from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        current_max_area = 0
        max_height = max(height)

        while l < r:
            current_max_area = max(current_max_area, (r-l)*min(height[l], height[r]))
            if(height[l] < height[r]):
                l+=1
            else:
                r-=1
            if current_max_area >= max_height * (r-l):
                break
        return current_max_area
            
