class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            ind = abs(nums[i])
            if ind - 1 >= 0 and ind - 1 < len(nums):
                if nums[ind - 1] == 0:
                    nums[ind - 1] = -len(nums)
                else:
                    nums[ind - 1] = abs(nums[ind - 1]) * -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1