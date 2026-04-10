class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        greedy algorithm

        1. initially had an idea of traversing thru prices, and keeping track of a min and a max (prices), and updating them while making sure the min_id is smaller than max_id
        2. however, this problem is designed to be solved in greedy, this is because: i only need the best profit so far, because i may sell at ANY day of the array, so i only need to keep track of the smallest buy in (never hurts the profit), the current max profit (update whenever it gets better from an updated buy price)
        
        43 ms runtime beats 70%
        """
        
        profit = 0
        buy_price = math.inf

        for price in prices:

            buy_price = min(buy_price, price)
            profit = max(profit, price - buy_price)

        return profit
