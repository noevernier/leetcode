from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        c2 = Counter(c.values())
        l = c2.values()
        for e in l:
            if e!=1:
                return False
        return True