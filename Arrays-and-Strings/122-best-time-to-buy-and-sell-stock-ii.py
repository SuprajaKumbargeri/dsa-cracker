# Link to Leetcode problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Same as below but using one less variable
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        # this optimization means we add at every consecutive increment in slopes
        
        return profit

        # TC: O(n)
        # SC: O(1)

        # The trick is realizing that you can buy and/or sell on any day
        # So buying on day 1 and selling on day 3 at a higher price than day 2
        # is same as buying on selling on days 1 and 2, and again on days 2 and 3
        # One pass -- considering every increasing slope difference
        '''
        profit = 0
        curr_min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > curr_min:
                profit += (prices[i] - curr_min)
            curr_min = prices[i] # --- > if we're doing this on every step means we're using the previous value each time. Why not use the (i-1)th index? 
        
        return profit
        '''