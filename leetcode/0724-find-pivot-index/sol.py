class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_of_nums = sum(nums)
        left = 0
        for i in range(len(nums)):
            if sum_of_nums - left - nums[i] == left:
                return i
            left += nums[i]
        return -1
