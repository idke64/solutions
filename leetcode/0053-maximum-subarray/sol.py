class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        psum = 0
        ans = nums[0]
        min_val = 0
        for i in range(len(nums)):
            psum += nums[i]
            ans = max(ans,psum - min_val)
            if psum < min_val:
                min_val = psum
                
        return ans
                