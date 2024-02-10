class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def recCountSubstring(s):
            if len(s)==1:
                return 1
            else:
                l, r = s[:-1], s[-1]
                res = recCountSubstring(l)+1
                c = r
                for e in l[::-1]:
                    c = e+c
                    if c == c[::-1]:
                        res+=1
                return res

        return recCountSubstring(s)