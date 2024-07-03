class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        prev_pos = nums[0]
        prev_neg = nums[0]
        for i in range(1,len(nums)):
            curr_pos = max(prev_pos + nums[i], prev_neg + nums[i])
            curr_neg = prev_pos - nums[i]
            prev_pos = curr_pos
            prev_neg = curr_neg
                        
        return max(prev_pos,prev_neg)