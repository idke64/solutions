class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first_min = nums[0]
        second_min = 2 ** 31 - 1
        for i in range(1,len(nums)):
            if nums[i] > second_min:
                return True
            if nums[i] < first_min:
                first_min = nums[i]
            if nums[i] < second_min and nums[i] > first_min:
                second_min = nums[i]
        return False