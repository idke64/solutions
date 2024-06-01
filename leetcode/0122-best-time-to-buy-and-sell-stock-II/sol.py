class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        prices.append(-1)
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                ans += prices[i-1] - buy_price
                buy_price = prices[i]

        return ans