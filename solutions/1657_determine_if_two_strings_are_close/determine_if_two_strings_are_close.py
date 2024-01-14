from typing import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        l1 = list(c1.values())
        l2 = list(c2.values())

        l1.sort()
        l2.sort()

        return c1.keys()==c2.keys() and l1==l2