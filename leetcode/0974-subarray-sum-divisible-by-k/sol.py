class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        m = {0 : 1}
        prev = 0
        for i in range(len(nums)):
            prev = (prev + nums[i]) % k
            if prev not in m:
                m[prev] = 1
            else:
                m[prev] += 1
        ans = 0
        for key in m:
            if m[key] > 1:
                ans += (m[key] * (m[key] - 1)) // 2
        return ans