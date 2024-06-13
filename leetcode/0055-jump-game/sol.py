class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            if max_jump == len(nums) - 1:
                return True
            if nums[i] == 0:
                if max_jump <= i:
                    return False
            max_jump = max(max_jump, i + nums[i])
        return True
