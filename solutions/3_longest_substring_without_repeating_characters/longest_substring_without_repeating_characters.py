class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)
        for i in range(n):
            current_length = 0
            j = i
            while j < n and (s[j] not in s[i:j]) :
                current_length+=1
                j+=1
            if max_length < current_length:
                max_length = current_length
        return max_length