from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        c = {k: v for k, v in sorted(c.items(), key=lambda item: item[1], reverse=True)}
        res = ""
        for e in c:
            res += e*c[e]
        return res