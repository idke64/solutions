class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        if 0 in nums:
            left = nums.index(0)
        else:
            return len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                right = len(nums) - i - 1
                for j in range(i + 1, len(nums)):
                    if nums[j] == 0:
                        right = j - i - 1
                        break
                ans = max(ans, right + left)
                left = right
                
        return ans