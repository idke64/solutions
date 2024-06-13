class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = {}
        count = 0
        for i in range(len(nums)):
            if k - nums[i] in m and m[k - nums[i]] > 0:
                m[k - nums[i]] -= 1
                count += 1
            else:
                if nums[i] in m:
                    m[nums[i]] += 1
                else:
                    m[nums[i]] = 1
        return count
