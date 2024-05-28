class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = []
        dp.append([[]])
        candidates.sort()
        for i in range(1, target + 1):
            dp.append([])
            for j in range(len(candidates)):
                if i - candidates[j] < 0:
                    break
                else:
                    for k in range(len(dp[i - candidates[j]])):
                        if len(dp[i-candidates[j]]) > 0 and (len(dp[i-candidates[j]][k]) == 0 or candidates[j] >= dp[i-candidates[j]][k][-1]):

                            temp = dp[i-candidates[j]][k].copy()
                            temp.append(candidates[j])
                            dp[i].append(temp)
        return dp[target]
                        