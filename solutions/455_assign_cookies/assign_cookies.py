from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_ptr = 0
        s_ptr = 0
        res = 0
        g.sort()
        s.sort()
        while g_ptr < len(g) and s_ptr < len(s):
            if g[g_ptr] <= s[s_ptr]:
                res += 1
                g_ptr += 1
                s_ptr += 1
            else:
                s_ptr += 1
        return res
