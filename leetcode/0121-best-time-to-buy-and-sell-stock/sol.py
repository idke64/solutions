class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > min_price:
                ans = max(ans, prices[i] - min_price)
            else:
                min_price = prices[i]
        return ans
        