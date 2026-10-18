class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        buy = 0
        sell = 1
        best = 0
        while sell < n:
            profit = prices[sell]-prices[buy]
            best = max(best, profit)
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1

        return best
