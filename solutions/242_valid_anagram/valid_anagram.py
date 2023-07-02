import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(list(s)) == collections.Counter(list(t))