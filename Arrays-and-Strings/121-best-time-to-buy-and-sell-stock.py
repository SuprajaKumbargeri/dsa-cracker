# Link to Leetcode problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, p: List[int]) -> int:
        profit = 0
        min_stock = p[0]
        for i in range(1, len(p)):
            if p[i] <= min_stock:
                min_stock = p[i]
            profit = max(profit, p[i] - min_stock)
        return profit
    
    # TC: O(n)
    # SC: O(1)