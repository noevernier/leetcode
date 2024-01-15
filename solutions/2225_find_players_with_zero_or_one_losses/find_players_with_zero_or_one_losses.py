from collections import Counter
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        losers = []

        for m in matches:
            winners.append(m[0])
            losers.append(m[1])

        winners_c = Counter(winners)
        losers_c = Counter(losers)

        unique_losers = [element for element, count in losers_c.items() if count == 1]

        best_winners = []
        for element, count in winners_c.items():
            if not losers_c[element]:
                best_winners.append(element)

        return sorted(best_winners), sorted(unique_losers)