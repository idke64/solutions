class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [nums[-1]]
        for i in range(1, len(nums)):
            right.insert(0,nums[len(nums) - 1 - i] * right[len(right) - i])
        for i in range(1,len(nums)):
            nums[i] *= nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                nums[i] = right[i+1]
                continue
            if i == len(nums) - 1:
                nums[i] = nums[i-1]
                continue
            nums[i] = nums[i-1] * right[i+1]
        return nums