class Solution:
    def numTilings(self, n: int) -> int:
        dp = []
        dp.append(1)
        dp.append(2)
        dp.append(5)
        mod = (10 ** 9) + 7
        for i in range(3,n):
            dp.append((((dp[i-1] * 2) % mod) + (dp[i-3] % mod)) % mod)
        return dp[n-1]