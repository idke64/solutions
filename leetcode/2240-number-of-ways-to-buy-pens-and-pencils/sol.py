class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        exp = max(cost1, cost2)
        chp = min(cost1, cost2)
        curr = 0
        ans = 0
        while total - (curr * exp) >= 0:
            ans += ((total - (curr * exp)) // chp) + 1
            curr += 1
        return ans