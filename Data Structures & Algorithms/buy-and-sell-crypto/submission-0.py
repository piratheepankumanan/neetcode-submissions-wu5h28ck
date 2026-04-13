class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            selling_price = prices[i]
            if i > 0:
                min_buy = min(prices[0:i])
            else: 
                min_buy = prices[0]
            if profit < (selling_price - min_buy):
                profit = selling_price - min_buy
        return profit