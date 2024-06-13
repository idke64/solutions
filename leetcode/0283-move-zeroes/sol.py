class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = 1
        i = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                right = max(right,i+1)
                while right < len(nums):
                    if nums[right] != 0:
                        nums[i] = nums[right]
                        nums[right] = 0
                        break
                    right += 1