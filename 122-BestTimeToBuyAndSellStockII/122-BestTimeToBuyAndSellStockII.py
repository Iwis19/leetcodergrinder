class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        very quick medium

        1. initially thought about just going thru arr start to end, see higher price than buy in, sell immediately, etc and repeat
        2. however, i saw the 2nd example 1 2 3 4 5 and thought that 2-1 + 4-3 + 0 = 2 bucks of profit, but i forgot that i could just do 2-1 + 3-2 + 4-3 + 5-4 = 4
        3. key insight is that sum of all positive consecutive differenes equal the sum of all peak-valley differences

        0 ms runtime beats 100
        """
        
        profit = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
