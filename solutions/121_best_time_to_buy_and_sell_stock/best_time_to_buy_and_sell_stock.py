from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        min_price = prices[0]

        for p in prices:
            if p-min_price > best_profit:
                best_profit = p-min_price
            if p < min_price:
                min_price = p
  
        return best_profit