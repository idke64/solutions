class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = int(grid[0][0] == 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    continue
                if i - 1 >= 0 and grid[i-1][j] != 1:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0 and grid[i][j-1] != 1:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]