class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n = len(s)
        freq = [0]*26

        for s_l, t_l in zip(s, t):
            freq[ord(t_l)-97] += 1
            freq[ord(s_l)-97] -= 1
        
        res = 0

        for f in freq:
            res += abs(f)

        return res//2

        


